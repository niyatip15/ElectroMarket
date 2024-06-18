// axiosConfig.js

import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://localhost:8000/api/',  
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'), 
    },
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export default instance;
