document.addEventListener('DOMContentLoaded', () => {
    const answerCards = document.querySelectorAll('.card[data-answer-id]');

    answerCards.forEach((card) => {
        const correctButton = card.querySelector('.mark-correct-button');
        const answerId = card.dataset.answerId;
        const correctIndicator = card.querySelector('.correct-indicator');

        if (correctButton) {
            correctButton.addEventListener('click', () => {
                const request = new Request(`/answers/${answerId}/mark_as_correct/`, {
                    method: 'POST',
                    headers: {
                        'x-CSRFToken': getCookie('csrftoken'),
                        'Content-Type': 'application/json',
                    },
                });

                fetch(request)
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.success) {
                            // Update button text and status
                            correctButton.textContent = data.is_correct ? 'Unmark as Correct' : 'Mark as Correct';
                            correctIndicator.style.display = data.is_correct ? 'block' : 'none';
                        }
                    })
                    .catch((error) => console.error('Error:', error));
            });
        }
    });
});