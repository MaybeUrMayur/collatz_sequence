from django.shortcuts import render
from django.http import JsonResponse
from .collatz_sequence import generate_collatz_sequence
from .models import CollatzHistory

def collatz_view(request):
    """Renders the Collatz sequence generator page."""
    return render(request, 'api/collatz.html')

def collatz_api(request):
    """API endpoint that returns the Collatz sequence as JSON."""
    try:
        n = request.GET.get('n')
        
        if not n:
            return JsonResponse({'error': 'Missing parameter: n'}, status=400)
        
        try:
            n = int(n)
        except ValueError:
            return JsonResponse({'error': 'Parameter n must be an integer'}, status=400)
        
        if n <= 0:
            return JsonResponse({'error': 'Please enter a strictly positive integer (greater than 0).'}, status=400)
        
        sequence = generate_collatz_sequence(n)
        total_steps = len(sequence) - 1
        max_value = max(sequence)
        
        # Save to database
        history_entry = CollatzHistory.objects.create(
            starting_number=n,
            sequence=sequence,
            total_steps=total_steps,
            max_value=max_value
        )
        
        return JsonResponse({
            'sequence': sequence,
            'steps': total_steps,
            'max_value': max_value,
            'id': history_entry.id
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def collatz_history(request):
    """API endpoint to retrieve Collatz sequence history."""
    try:
        # Get all history entries, most recent first
        history = CollatzHistory.objects.all()[:50]  # Limit to last 50 entries
        
        history_data = [
            {
                'id': entry.id,
                'starting_number': entry.starting_number,
                'total_steps': entry.total_steps,
                'max_value': entry.max_value,
                'created_at': entry.created_at.isoformat(),
                'sequence': entry.sequence
            }
            for entry in history
        ]
        
        return JsonResponse({
            'history': history_data,
            'count': len(history_data)
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def collatz_history_detail(request, history_id):
    """API endpoint to retrieve a specific history entry."""
    try:
        entry = CollatzHistory.objects.get(id=history_id)
        
        return JsonResponse({
            'id': entry.id,
            'starting_number': entry.starting_number,
            'sequence': entry.sequence,
            'total_steps': entry.total_steps,
            'max_value': entry.max_value,
            'created_at': entry.created_at.isoformat()
        })
    
    except CollatzHistory.DoesNotExist:
        return JsonResponse({'error': 'History entry not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
