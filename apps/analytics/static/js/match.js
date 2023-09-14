document.querySelectorAll('.toggle-favorite').forEach(function (button) {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        var matchId = this.getAttribute('data-match-id');

        fetch(`/toggle_favorite/${matchId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.setAttribute('data-favorite', !isFavorite);
                    if (!isFavorite) {
                        this.textContent = 'Удалить из избранного';
                    } else {
                        this.textContent = 'Добавить в избранное';
                    }
                }
            })
            .catch(error => {
                console.error('Ошибка при выполнении запроса:', error);
            });
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}