# **Git Kurs** 19.03.2025 - 21.03.2025

1. [Grundlagen](#grundlagen)
2. [Status](#status)
3. [Add](#add)
4. [Commit](#commit)
5. [Diff](#diff)
6. [gitignore](#gitignore)
7. [Fetch](#fetch)
8. [Pull](#pull)
9. [Push](#push)
10. [Branches](#branches)
11. [Switch](#switch)
12. [Issues](#issues)
13. [Pull request](#pull-request)
14. [Stash](#stash)
15. [Tags](#tags)
16. [Rebase](#rebase)
17. [Merge](#merge)
18. [Reset](#reset)
19. [Revert](#revert)
20. [Log](#log)
21. [Remote](#remote)
22. [Cherry-pick](#cherry-pick)

### Grundlagen
Wie funktioniert was?  
Wieso Git?  

### Status
`git status`  
Zeigt den aktuellen Status des Projekts an, einschließlich der Änderungen, die zur Staging-Area hinzugefügt wurden, und der Änderungen, die noch nicht gestaged wurden.

### Add
`git add <datei>`  
Fügt eine Datei zur Staging-Area hinzu, sodass sie beim nächsten Commit eingeschlossen wird.

`git add .`  
Fügt alle Änderungen im aktuellen Verzeichnis zur Staging-Area hinzu.

### Commit
`git commit -m "Commit-Nachricht"`  
Speichert die Änderungen in der Staging-Area dauerhaft im Repository mit einer beschreibenden Nachricht.

`git commit -a -m "Commit-Nachricht"`  
Fügt alle geänderten Dateien zur Staging-Area hinzu und committet sie in einem Schritt.

### Diff
`git diff`  
Zeigt die Unterschiede zwischen den Arbeitsverzeichnis-Dateien und den zuletzt committeten Dateien an.

`git diff --staged`  
Zeigt die Unterschiede zwischen den Dateien in der Staging-Area und den zuletzt committeten Dateien an.

### gitignore
Eine `.gitignore`-Datei wird verwendet, um Dateien und Verzeichnisse zu definieren, die Git

### Grundlagen
Wie funktioniert was?  
Wieso Git?  

### Status
`git status`  
Zeigt den aktuellen Status des Projekts an, einschließlich der Änderungen, die zur Staging-Area hinzugefügt wurden, und der Änderungen, die noch nicht gestaged wurden.

### Add
`git add <datei>`  
Fügt eine Datei zur Staging-Area hinzu, sodass sie beim nächsten Commit eingeschlossen wird.

`git add .`  
Fügt alle Änderungen im aktuellen Verzeichnis zur Staging-Area hinzu.

### Commit
`git commit -m "Commit-Nachricht"`  
Speichert die Änderungen in der Staging-Area dauerhaft im Repository mit einer beschreibenden Nachricht.

`git commit -a -m "Commit-Nachricht"`  
Fügt alle geänderten Dateien zur Staging-Area hinzu und committet sie in einem Schritt.

### Diff
`git diff`  
Zeigt die Unterschiede zwischen den Arbeitsverzeichnis-Dateien und den zuletzt committeten Dateien an.

`git diff --staged`  
Zeigt die Unterschiede zwischen den Dateien in der Staging-Area und den zuletzt committeten Dateien an.

### gitignore
Eine `.gitignore`-Datei wird verwendet, um Dateien und Verzeichnisse zu definieren, die Git ignorieren soll. Dies ist nützlich, um temporäre Dateien oder Build-Artefakte vom Repository fernzuhalten.

Beispiel `.gitignore`:
**Ignoriere alle .log Dateien**
*.log

**Ignoriere das Verzeichnis tmp/**
tmp/


### Fetch
`git fetch`  
Holt die neuesten Änderungen vom Remote-Repository, ohne sie in das aktuelle Branch zu mergen. Die Änderungen werden in den Remote-Tracking-Branches gespeichert.

### Pull
`git pull`  
Holt die neuesten Änderungen vom Remote-Repository und merged sie in das aktuelle Branch. Dies ist eine Kombination aus `git fetch` und `git merge`.

### Push
`git push`  
Lädt die lokalen Commits zum Remote-Repository hoch. Dies aktualisiert das Remote-Repository mit den neuesten Änderungen aus dem lokalen Repository.

### Branches
`git branch <branch-name>`  
Erstellt einen neuen Branch mit dem angegebenen Namen. Ein Branch ist ein paralleler Entwicklungszweig, der aus dem aktuellen Stand des Master-Branches erstellt wird.

`git branch`  
Listet alle lokalen Branches auf und zeigt den aktuellen Branch an.

### Switch
`git switch <branch-name>`  
Wechselt in den angegebenen Branch.

`git switch -c <branch-name>`  
Erstellt einen neuen Branch und wechselt direkt in diesen Branch.

### Issues
Über Issues können "User Stories" oder Anforderungen erstellt werden. Sie dienen dazu, Aufgaben zu verfolgen und zu verwalten.

- **Issue erstellen**: Gehen Sie zu Ihrem Repository auf GitHub und klicken Sie auf "Issues" und dann auf "New issue".
- **Issue schließen**: Kommentieren Sie den Issue mit `closes #<issue-number>` oder `fixes #<issue-number>` in Ihrem Commit, um den Issue automatisch zu schließen.

### Pull request
Ein Pull Request kann von einem Entwickler erstellt werden, der seinen Branch mit dem Main-Branch zusammenführen möchte. Der Reviewer kann während des Review-Prozesses Verbesserungen vorschlagen oder den Pull Request genehmigen.

- **Pull Request erstellen**: Gehen Sie zu Ihrem Repository auf GitHub, wechseln Sie zum gewünschten Branch und klicken Sie auf "New pull request".
- **Pull Request überprüfen und mergen**: Überprüfen Sie den Pull Request und klicken Sie auf "Merge pull request", um die Änderungen zu mergen.

### Stash
`git stash`  
Speichert uncommittete Änderungen temporär, um sie später wiederherstellen zu können. Dies ist nützlich, wenn Sie an etwas arbeiten und zu einem anderen Branch wechseln müssen, ohne Ihre Änderungen zu committen.

`git stash apply`  
Wendet die zuletzt gestashten Änderungen wieder an.

`git stash list`  
Listet alle gestashten Änderungen auf.

`git stash drop`  
Löscht den zuletzt erstellten Stash.

### Tags
Tags werden verwendet, um bestimmte Punkte in der Historie eines Repositories zu markieren, normalerweise um Releases zu kennzeichnen.

- **Tag erstellen**: `git tag <tag-name>`
- **Tag erstellen mit Nachricht**: `git tag -a <tag-name> -m "Nachricht"`
- **Tags anzeigen**: `git tag`
- **Tag zu Remote Repository pushen**: `git push origin <tag-name>`
- **Alle Tags zu Remote Repository pushen**: `git push origin --tags`
- **Tag löschen**: `git tag -d <tag-name>`
- **Remote Tag löschen**: `git push origin --delete <tag-name>`

### Rebase
`git rebase <branch>`  
Wendet die Änderungen des aktuellen Branches auf den angegebenen Branch an. Dies wird oft verwendet, um eine saubere, lineare Commit-Historie zu erstellen.

### Merge
`git merge <branch>`  
Führt die Änderungen des angegebenen Branches in den aktuellen Branch zusammen.

### Reset
`git reset <commit>`  
Setzt den aktuellen Branch auf den angegebenen Commit zurück. Dies kann verwendet werden, um Commits rückgängig zu machen.

`git reset --hard <commit>`  
Setzt den aktuellen Branch auf den angegebenen Commit zurück und verwirft alle Änderungen im Arbeitsverzeichnis und in der Staging-Area.

### Revert
`git revert <commit>`  
Erstellt einen neuen Commit, der die Änderungen des angegebenen Commits rückgängig macht. Dies wird verwendet, um Änderungen rückgängig zu machen, ohne die Commit-Historie zu ändern.

### Log
`git log`  
Zeigt die Commit-Historie des Repositories an.

`git log --oneline`  
Zeigt die Commit-Historie in einer kompakten, einzeiligen Darstellung an.

`git log --graph --oneline --all`  
Zeigt die Commit-Historie als Graph in einer kompakten, einzeiligen Darstellung an.

### Remote
`git remote add <name> <url>`  
Fügt ein Remote-Repository hinzu.

`git remote -v`  
Zeigt die URLs der Remote-Repositories an.

`git remote remove <name>`  
Entfernt ein Remote-Repository.

### Cherry-pick
`git cherry-pick <commit>`  
Wendet die Änderungen des angegebenen Commits auf den aktuellen Branch an. Dies wird verwendet, um spezifische Änderungen aus einem anderen Branch zu übernehmen.
