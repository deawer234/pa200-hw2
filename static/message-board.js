/**
 * message-board.js - External JavaScript for the Message Board application
 * To be hosted on Azure Blob Storage
 */

document.addEventListener('DOMContentLoaded', function() {
    // Update the message count
    const messageContainer = document.getElementById('message-container');
    const messageCountElement = document.getElementById('message-count');
    const messages = messageContainer.querySelectorAll('.message');
    
    updateMessageCount(messages.length);
    
    // Add animation effects to messages
    messages.forEach(message => {
        addHoverEffect(message);
    });
    
    // Add timestamp and formatting to messages
    messages.forEach(message => {
        enhanceMessage(message);
    });
    
    // Function to update the message count
    function updateMessageCount(count) {
        messageCountElement.textContent = `Total Messages: ${count}`;
    }
    
    // Function to add hover effects to messages
    function addHoverEffect(messageElement) {
        messageElement.addEventListener('mouseover', function() {
            this.style.backgroundColor = '#f5f5f5';
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
            this.style.transition = 'all 0.3s ease';
        });
        
        messageElement.addEventListener('mouseout', function() {
            this.style.backgroundColor = '';
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    }
    
    // Function to enhance message appearance
    function enhanceMessage(messageElement) {
        // Add a timestamp
        const timestamp = document.createElement('div');
        timestamp.className = 'timestamp';
        timestamp.textContent = `Posted on: ${new Date().toLocaleDateString()}`;
        timestamp.style.fontSize = '0.8em';
        timestamp.style.color = '#666';
        timestamp.style.marginTop = '5px';
        
        messageElement.appendChild(timestamp);
        
        // Apply text formatting
        const content = messageElement.childNodes[0];
        const formattedText = content.textContent
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')  // Bold
            .replace(/\*(.*?)\*/g, '<em>$1</em>');             // Italic
        
        // Create a container for the formatted text
        const formattedContent = document.createElement('div');
        formattedContent.innerHTML = formattedText;
        
        // Replace original text with formatted version
        messageElement.insertBefore(formattedContent, content);
        content.remove();
    }
});