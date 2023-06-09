# Comparer les couleurs

Pour plus de précision à reconnaître les couleurs avec le capteur de couleur, c'est parfois
nécessaire d'utiliser la commande `cs.rgb()` au lieu de `cs.color()` - où `cs` est définie
comme un `ColorSensor` dans le programme.

## Limites de color()

La commande `color()` retourne une valeur parmi un nombre de couleurs prédéfinies. Le problème 
arrive si, par exemple, `Color.BLUE` n'est pas exactement le même bleu que vous mesurez.

## Possibilités avec rgb()

Les couleurs sont stockées en informatique - comme dans les ordinateurs, les cellulaires et votre
EV3 - comme un *tuple* de trois valeurs : une pour le rouge, une pour le vert et une pour le bleu. C'est
ce qu'on appelle une couleur RGB (ou RVB en français).

Voici quelques exemples de valeurs pour des couleurs communes :

Couleur | Tuple RGB
--- | ---
Rouge | (255, 0, 0)
Vert | (0, 255, 0)
Bleu | (0, 0, 255)
Jaune | (255, 255, 0)
Cyan | (0, 255, 255)
Magenta | (255, 0, 255)

Mais les objets réels (comme les cartons ou le ruban adhésif) ne donnent pas nécessairement ces valeurs
exactement ou peuvent donner différentes valeurs selon les conditions d'éclairage.

### Mesurer la couleur réelle

On peut alors utiliser `print(cs.rgb())` dans une boucle infinie - où `cs` est encore un ColorSensor - et placer nos objets réels devant le capteur pour voir les valeurs R, G et B qui sont mesurées. Dans l'exemple de code on a mesuré deux cartons, un jaune et un bleu. On a déclaré un tuple pour chacun avec les lignes suivantes.

```python
# Couleurs RGB  - mesurés avec print(color_sensor.rgb())
yellow = (55, 33, 38)
blue = (23, 54, 153) 
```

>Notez que c'est `print(color_sensor.rgb())` - et non `cs.rgb()` - parce que le capteur couleur est nommé `color_sensor` dans le programme

### Comparer des tuples

Voici l'algorithme pour comparer les tuples afin de voir si chaque valeur est identique :

```
Lire la première valeur mesurée et voir si elle est égale à la première valeur de référence.
Lire la deuxième valeur mesurée et voir si elle est égale à la deuxième valeur de référence.
Lire la troisième valeur mesurée et voir si elle est égale à la troisième valeur de référence.
```

Avec **une boucle** on peut utiliser une **variable d'index** pour représenter la 1e, 2e et 3e valeur comme ceci :

```
Assigner à i la valeur 1
Répéter trois fois :
    Lire la valeur i dans le tuple mesurée et voir si elle est égale à la valeur i du tuple de référence.
    Augmenter i de 1
```

### Inclure une marge d'erreur

Parce que les capteurs incluent toujours de l'incertitude dans ses mesures et parce que les conditions autour d'un robot sont variables, c'est très rare que les trois valeurs mesurées seront exactement les mêmes que les trois valeurs de référence. La solution est de remplacer la comparaison directe `mesure == référence` avec quelque chose de plus flexible : comparer `(mesure - référence) < écart acceptable`, soit vérifier si la différence entre les deux valeurs est acceptable ou non.

Parce que la mesure peut être plus grande ou plus petite que la référence, il faut ajouter une dernière modification à la comparaison : on compare la **valeur absolue** de la différence avec l'écart acceptable. La valeur absolue est une opération mathématique qui élimine le signe négatif. Donc pour vérifier **si deux valeurs sont les mêmes** on a maintenant la comparaison :

```
abs(mesure - référence) < écart acceptable
```

La comparaison inverse nous donne vrai **si les deux valeurs ne sont PAS les mêmes** :

```
abs(mesure - référence) >= écart acceptable
```

### Mettre le tout ensemble

**Les deux couleurs sont les mêmes, tenant compte d'une marge d'erreur acceptable, seulement si les trois comparaisons sont vraies.**

Un algorithme classique pour ce genre d'analyse est la suivante. Elle présume que les valeurs sont les mêmes, mais change le constat et cesse les comparaisons si l'écart est trop grand lors d'une seule comparaison. Ainsi la variable qui spécifie l'égalité reste vraie seulement si toutes les comparaisons sont acceptables.

```
Assigner à same_values la valeur True
Pour toutes les valeurs dans mesure et dans référence :
    Si abs(valeur dans mesure - valeur dans référence) >= écart acceptable :
        Assigner à same_values la valeur False
        Quitter la boucle
Afficher same_values
```

Cette algorithme affichera True ou False pour indiquer si les deux tuples sont pareils ou non.

### Implémentation avec Python

Dans Python, comme la plupart des langages incluant Arduino, les **index commencent à 0**. Pour trois valeurs on aura alors les index 0, 1 et 2.

Une façon de générer ces valeurs dans Python est avec la fonction `range(n)`, où `n` est le nombre de valeurs voulues. Pour les tuples RGB, on veut trois valeurs alors on utiliserait `range(3)`, ce qui génère les valeurs 0, 1 et 2.

Pour accéder à une valeur spécifique dans un tuple, on utilise la notation `nom[index]`, p.ex. : `rgb_measured[0]` est la première valeur dans le tuple `rgb_measured`.

Finalement, on peut utiliser une variable pour stocker la valeur de l'index. Souvent on utilise la lettre `i` comme variable d'index.

Le code dans main.py pour comparer les valeurs est donc :

```python
err = 5 # écart acceptable

for i in range(3):
    if abs(rgb_target[i] - rgb_measured[i]) >= err :
        return False
return True
```

Ce code se trouve dans une fonction (`same_colors(rgb_target)`), alors le mot-clé `return` met immédiatement fin à la fonction. Ainsi la fonction retournera toujours `False` si la différence est trop grande. Seulement si on a réussi à comparer les trois valeurs avec un écart plus petit que la valeur `err` est-il possible de se rendre à l'instruction `return True`.

On appelle cette fonction dans la boucle principale du programme et on utilise la valeur retournée (True ou False) pour décider si la brique EV3 dira le nom de la couleur ou non.

```python
if same_color_as(yellow) :
    ev3.speaker.say("yellow")
elif same_color_as(blue) :
    ev3.speaker.say("blue")
```
