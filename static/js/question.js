function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies [i]. trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent (cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const cards = document.getElementsByClassName('card');
const question = document.getElementsByClassName('question-body').item(0);
const questionId = question.dataset.questionId;

const questionLikeButton = document.getElementsByClassName('question-like').item(0);
const questionDislikeButton = document.getElementsByClassName('question-dislike').item(0);
const quesstionLikesCount = document.querySelector('.question-likes-count')

for (const card of cards) {

    const likeButton = card.querySelector('.like-button');
    const dislikeButton = card.querySelector('.dislike-button');

    const likesCount = card.querySelector('.likes-count')
    const answerId = card.dataset.answerId

    likeButton.addEventListener('click', () => {
        const request = new Request (`/like_answer/${answerId}`, {
            method: "POST",
            headers: {'x-CSRFToken': getCookie('csrftoken')},
            body: JSON.stringify({type: "like"}),
        });

        fetch(request).then((response) => {
            response.json().then((data) => {
                likesCount.innerHTML = data.likes_count ?? 0;
            })
        });
    });
    dislikeButton.addEventListener('click', () => {
        const request = new Request (`/like_answer/${answerId}`, {
            method: "POST",
            headers: {'x-CSRFToken': getCookie('csrftoken')},
            body: JSON.stringify({type: "dislike"}),
        });

        fetch(request).then((response) => {
            response.json().then((data) => {
                likesCount.innerHTML = data.likes_count ?? 0;
            })
        });
    });
}


questionLikeButton.addEventListener('click', () => {
    const request = new Request (`/${questionId}/like_question`, {
        method: "POST",
        headers: {'x-CSRFToken': getCookie('csrftoken')},
        body: JSON.stringify({type: "like"}),
    });

    fetch(request).then((response) => {
        console.log({response})
        response.json().then((data) => {
            quesstionLikesCount.innerHTML = data.likes_count ?? 0;
        })
    });
});


questionDislikeButton.addEventListener('click', () => {
    const request = new Request (`/${questionId}/like_question`, {
        method: "POST",
        headers: {'x-CSRFToken': getCookie('csrftoken')},
        body: JSON.stringify({type: "dislike"}),
    });

    fetch(request).then((response) => {
        response.json().then((data) => {
            quesstionLikesCount.innerHTML = data.likes_count ?? 0;
        })
    });
});