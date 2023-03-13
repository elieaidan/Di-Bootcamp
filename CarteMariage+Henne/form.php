<?php
// Vérifier si le formulaire a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Récupérer les données du formulaire
    $nom = $_POST["nom"];
    $presenceHenne = $_POST["presenceHenne"];
    $presenceMariage = $_POST["presenceMariage"];
    $nombreHenne = $_POST["nombreHenne"];
    $nombreMariage = $_POST["nombreMariage"];

    // Construire la ligne à écrire dans le fichier
    $ligne = "$nom,$presenceHenne,$presenceMariage,$nombreHenne,$nombreMariage\n";

    // Ouvrir le fichier en mode écriture, en ajoutant les données à la fin
    $fichier = fopen("reponses-mariage.csv", "a");

    // Écrire la ligne dans le fichier
    fwrite($fichier, $ligne);

    // Fermer le fichier
    fclose($fichier);

    // Rediriger vers une page de confirmation
    header("Location: confirmation.html");
    exit();
}
?>
