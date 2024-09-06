// Handle URL shortening
document.getElementById('shorten-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const originalUrl = document.getElementById('original_url').value;
    const length = document.getElementById('length').value;

    const response = await fetch('/shorten/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ original_url: originalUrl, length: parseInt(length) })
    });

    const result = await response.json();
    document.getElementById('result').innerHTML = `Shortened URL: <a href="${result.shortened_url}">${result.shortened_url}</a>`;
});

// Handle URL update
document.getElementById('update-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const shortUrl = document.getElementById('short_url').value;
    const newUrl = document.getElementById('new_url').value;
    const newLength = document.getElementById('new_length').value;

    const response = await fetch(`/${shortUrl}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ original_url: newUrl, length: newLength ? parseInt(newLength) : undefined })
    });

    const result = await response.json();
    document.getElementById('manage-result').innerHTML = `Updated URL: <a href="${result.updated_url}">${result.updated_url}</a>`;
});

// Handle URL deletion
document.getElementById('delete-btn').addEventListener('click', async function() {
    const shortUrl = document.getElementById('short_url').value;

    const response = await fetch(`/${shortUrl}`, {
        method: 'DELETE'
    });

    const result = await response.json();
    document.getElementById('manage-result').innerHTML = result.detail;
});

