---
title: Ouverture du dossier dans le devcontainer
---

# Ouverture du dossier dans le _container_

Rouvrez le dossier de votre site dans le _devcontainer_. Vous avez plusieurs moyens de le faire:

1. Vous pouvez cliquer sur l'icône en bas à gauche de votre écran:
   <img src="../static/img/remote_icon.png" style="vertical-align: middle; height: 1.2em"/>
   et cliquez sur _Reopen in Container_.
2. Vous pouvez aussi ouvrir la palette de commande avec ++ctrl+shift+p++ ou ++cmd+shift+p++ et cherchez _Remote-Containers: Reopen in Container_. 
3. Vous pouvez enfin fermer l'éditeur et le rouvrir.
   VS Code vous proposera de le rouvrir dans un container:
   <br/>
   ![Image description](../static/img/reopen.png){ width="75%" }

Vous savez que vous travaillez dans un container si en bas à gauche, la barre d'état de vs-code affiche le contenu suivant: <img src="../static/img/mkdocs_edu_status.png" style="vertical-align: middle; height: 1.2em"/>

Ouvrez un terminal dans vs-code et tapez la commande `mkdocs --version`. Vous devriez observer quelque chose comme ça: 

![Image description](../static/img/terminal.png){ width="100%" }
