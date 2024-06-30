$(document).ready(function(){
    // Function to load chat history
    function loadChatHistory() {
        $.ajax({
            type: 'GET',
            url: chatHistoryUrl,  // Utilisation de l'URL définie dans le template
            success: function(response) {
                if (response && response.length > 0) {
                    response.forEach(function(message) {
                        if (message.sender === 'user') {
                            $('#chat-box').append('<div class="user-message">' + message.text + '</div>');
                        } else if (message.sender === 'bot') {
                            $('#chat-box').append('<div class="bot-response">' + message.text + '</div>');
                        }
                    });
                }
            },
            error: function(xhr, status, error) {
                console.error('Failed to load chat history:', error);
            }
        });
    }

    // Call the function to load chat history on page load
    loadChatHistory();

    // Function to handle form submission
    $('#chat-form').on('submit', function(event){
        event.preventDefault();
        var userInput = $('#user-input').val();
        $.ajax({
            type: 'POST',
            url: chatbotUrl,  // Utilisation de l'URL définie dans le template
            data: {
                'user_input': userInput,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function(response){
                $('#chat-box').append('<div class="user-message">' + userInput + '</div>');
                $('#chat-box').append('<div class="bot-response">' + response.response + '</div>');
                $('#user-input').val('');
            },
            error: function(xhr, status, error) {
                console.error('Failed to send message:', error);
            }
        });
    });
});
