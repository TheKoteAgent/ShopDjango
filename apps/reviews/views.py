from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from apps.main.models import Lot
from .models import Review
from .forms import ReviewsForm

@login_required
@require_POST
def add_review(request, lot_id):
    lot = get_object_or_404(Lot, id=lot_id)
    form = ReviewsForm(request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        review.lot = lot
        review.author = request.user
        review.save()

    return redirect('main:lot_detail', lot_id=lot.id)


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.author:
        review.delete()

    return redirect('main:lot_detail', lot_id=review.lot.id)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.author:
        return redirect('main:lot_detail', lot_id=review.lot.id)

    if request.method == 'POST':
        form = ReviewsForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('main:lot_detail', lot_id=review.lot.id)
    else:
        form = ReviewsForm(instance=review)

    return render(request, 'reviews/edit_review.html', {
        'form': form,
        'lot': review.lot
    })