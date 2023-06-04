# La sécurité des moteurs

## Comprendre `stall_example`

La ligne critique dans `stall_example` est celle-ci :

```python
stall_angle = motor.run_until_stalled(SPEED, then = Stop.HOLD, duty_limit = 75)
```

Le moteur utilise `run_until_stalled` comme commande d'opération. Cette commande prend 1 paramètre obligatoire et 2 paramètres nommés/optionnels :
* la vitesse de rotation du moteur (obligatoire)
* quoi faire quand le moteur arrête (le paramètre optionnel `then`). Par défaut c'est `Stop.COAST` (qui laisse le moteur tourné librement). Ici, j'ai choisi `Stop.HOLD` (qui maintient la position du moteur) parce que je veux saisir l'angle d'arrêt avec précision. Ce serait aussi une bonne option pour un bras robotique.
* la puissance maximale du moteur durant l'opération (le paramètre optionnel `duty_limit`). Par défaut, aucune valeur n'est assignée, mais j'ai spécifié 75 (pour 75%) afin de protéger le moteur davantage.

Finalement, `run_until_stalled` renvoie la valeur de l'angle du moteur mesuré lorsqu'il s'arrête et on conserve cette valeur dans une variable que j'ai nommée `stall_angle`. J'utilise cette angle comme référence pour des mouvements subséquents du moteur.

## Comprendre `manual_stall`

Dans cette exemple, on utilise des commandes moteurs plus directes, mais en échange nous devons spécifier la logique d'arrêt nous-même. Cela se passe dans une boucle while :

```python
while True  :
    motor.run(-SPEED)
    wait(60)
    if (motor.speed() == 0) :
        motor.hold()
        break
stall_angle = motor.angle()
```

Dans la boucle, on lance la commande `run` avec une vitesse. Ici le `-SPEED` signifie qu'on tourne le moteur dans la direction inverse que dans l'exemple avec `run_until_stalled`.

Ensuite on attend 60 millisecondes (`wait(60)`). Selon mes tests, cela semble être près du temps minimal requis pour démarrer le moteur afin que sa vitesse ne soit pas 0 pour la première vérification.

Finalement, avant de refaire la boucle on vérifie si la vitesse est nulle, soit si le moteur est bloqué, avec la condition `motor.speed() == 0`. Si oui, on dit au moteur de s'arrêter en maintenant sa position (`motor.hold()`) et on quitte aussi la boucle (`break`). Si non, on répète la boucle. Cela donne un comportement où le moteur tourne jusqu'à ce qu'il soit bloqué.

Pour enregistrer l'angle à cette position bloquée, on mesure l'angle avec `motor.angle()` et on assigne la valeur à la variable `stall_angle`.

## La reste de chaque exemple

Le reste de chaque exemple est identique. Voici le pseudocode :

```
Remet l'angle du moteur à 0
Bouge le moteur jusqu'à ce qu'il bloque et conserve l'angle de blocage dans stall_angle
Émet un son et attend quelques instants
Tourne le moteur jusqu'à ce que l'angle soit zéro (position de départ)
Émet un son et attend quelques instants
Tourne le moteur dans le sens opposé jusqu'à 95% de stall_angle
Émet un son et attend quelques instants
```

J'utilise 95% de `stall_angle` et non 100% pour éviter de forcer le moteur contre l'objet qui l'avait bloqué. Vous devrez observer que sa position finale est, à toutes fins pratiques, exactement la même que s'il avait frappé la barrière mais l'usure sur le moteur est éliminé.
