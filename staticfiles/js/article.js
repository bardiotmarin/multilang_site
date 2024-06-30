$(document).ready(function() {
    var unsplashImagesUrl = '/get-unsplash-images/';

    // Charger les images de Unsplash initialement
    loadUnsplashImages();

    // Charger les images de Unsplash en fonction de la recherche utilisateur
    $('#id_search_query').on('change', function() {
        loadUnsplashImages();
    });

    // Charger les images de Unsplash après avoir cliqué sur le bouton Search
    $('#search_button').on('click', function(event) {
        event.preventDefault();
        loadUnsplashImages();
    });

    // Fonction pour charger les images de Unsplash
    function loadUnsplashImages() {
        var searchQuery = $('#id_search_query').val();

        $.ajax({
            url: unsplashImagesUrl,
            data: {
                'search_query': searchQuery
            },
            success: function(data) {
                $('#id_stock_image').html(data);
                $('#selected_image_preview').attr('src', ''); // Réinitialiser l'image sélectionnée
            },
            error: function(xhr, status, error) {
                console.error('Failed to fetch images from Unsplash:', error);
            }
        });
    }

    // Mettre à jour l'image de prévisualisation lorsque l'utilisateur sélectionne une image
    $('#id_stock_image').on('change', function() {
        var selectedImageUrl = $(this).val();
        if (selectedImageUrl) {
            $('#selected_image_preview').attr('src', selectedImageUrl);
        } else {
            $('#selected_image_preview').attr('src', '');
        }
    });

    // Soumission du formulaire via AJAX
    $('#articleForm').on('submit', function(event) {
        event.preventDefault(); // Empêcher la soumission du formulaire par défaut

        $.ajax({
            url: $(this).attr('action'),
            method: $(this).attr('method'),
            data: $(this).serialize(),
            success: function(response) {
                // Rediriger vers une nouvelle page après une soumission réussie
                window.location.href = response.redirect_url;
            },
            error: function(xhr, status, error) {
                console.error('Failed to submit form:', error);
            }
        });
    });
});
