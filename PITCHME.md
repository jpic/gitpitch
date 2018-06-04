|-|-|-|
|0|1|0|
|-|-|-|
|0|0|1|
|-|-|-|
|1|1|1|
|-|-|-|

# Algorithmie
### Formation

---
## Principes generaux

- Un algorithme est une suite finie et non ambiguë d’opérations ou d'instructions permettant de résoudre un problème ou d'obtenir un résultat |
- Un problème est un objet mathématique qui représente une question ou un ensemble de questions auxquelles un ordinateur devrait être en mesure de répondre. |

---
- L'algorithmique est l'étude et la production de règles et techniques qui sont impliquées dans la définition et la conception d'algorithmes, |
- c'est-à-dire de processus systématiques de résolution d'un problème permettant de décrire précisément des étapes pour résoudre un problème algorithmique. |
- Un algorithme prend des données en entrées et calcule des données en retour |

---

## Antiquité

- Les premiers algorithmes dont on a retrouvé des descriptions datent des Babyloniens, au IIIe millénaire av. J.-C.. Ils décrivent des méthodes de calcul et des résolutions d'équations à l'aide d'exemples. |
- Un algorithme célèbre est celui qui se trouve dans le livre 7 des Éléments d'Euclide, et appelé algorithme d'Euclide. Il permet de trouver le plus grand diviseur commun, ou PGCD, de deux nombres. |

---
C'est Archimède qui proposa le premier un algorithme pour le calcul de $$π^2$$

---
## Étude systématique

- Le premier à avoir systématisé des algorithmes est le mathématicien perse Al-Khwârizmî, actif entre 813 et 833. |
- Dans son ouvrage Abrégé du calcul par la restauration et la comparaison, il étudie toutes les équations du second degré et en donne la résolution par des algorithmes généraux. |

---

- Il utilise des méthodes semblables à celles des Babyloniens, mais se différencie par ses explications systématiques là où les Babyloniens donnaient seulement des exemples. |
- Le mot algorithme vient du nom du mathématicien Al-Khwârizmî (latinisé au Moyen Âge en Algoritmi), qui, au IXe siècle écrivit le premier ouvrage systématique donnant des solutions aux équations linéaires et quadratiques. Algorithme a donné algorithmique auxquels certains préfèrent le néologisme algorithmie. |

---

Le savant andalou Averroès (1126-1198) évoque une méthode de raisonnement où la thèse s’affine étape par étape, itérativement, jusqu’à une certaine convergence et ceci conformément au déroulement d’un algorithme. À la même époque, au XIIe siècle, le moine Adelard de Bath introduit le terme latin de algorismus, par référence au nom de Al Khuwarizmi. Ce mot donne algorithme en français en 1554.

---

- Au XVIIe siècle, on pourrait entrevoir une certaine allusion à la méthode algorithmique chez René Descartes dans la méthode générale proposée par le Discours de la méthode (1637), notamment quand, en sa deuxième partie, le mathématicien français propose |
- « diviser chacune des difficultés que j’examinerois, en autant de parcelles qu’il se pourroit, et qu’il seroit requis pour les mieux résoudre. » |

---
- Sans évoquer explicitement les concepts de boucle, d’itération ou de dichotomie, l’approche de Descartes prédispose la logique à accueillir le concept de programme, mot qui naît en français en 1677.
- En 1843 , la mathématicienne et pionnière des sciences informatique Ada Lovelace, fille de Lord Byron et assistante de Charles Babbage réalise la première implémentation d'un algorithme sous forme de programme (calcul des nombres de Bernoullii) |
---

Le dixième problème de Hilbert qui fait partie de la liste des 23 problèmes posés par David Hilbert en 1900 à Paris est clairement un problème algorithmique. En l'occurrence, la réponse est qu'il n'y a pas d'algorithme répondant au problème posé.

---

### L'époque contemporaine

- L’algorithmique des XXe et XXIe siècles a pour fondement mathématique des formalismes, par exemple celui des machines de Turing, qui permettent de définir précisément ce qu'on entend par "étapes", par "précis" et par "non ambigu" et qui donnent un cadre scientifique pour étudier les propriétés des algorithmes.

---

Cependant, suivant le formalisme choisi on obtient des approches algorithmiques différentes pour résoudre un même problème. Par exemple l'algorithmique récursive, l'algorithmique parallèle ou l’informatique quantique donnent lieu à des présentations d'algorithmes différentes de celles de l'algorithmique itérative.

---

Grâce à l'informatique, l'algorithmique s'est beaucoup développée dans la deuxième moitié du XXe siècle. Donald Knuth, auteur du traité The Art of Computer Programming, qui décrit de très nombreux algorithmes, a contribué, avec d'autres, à en poser les fondements mathématiques de leur analyse.

---

### Heuristiques

Pour certains problèmes, les algorithmes ont une complexité beaucoup trop grande pour obtenir un résultat en temps raisonnable, même si l’on pouvait utiliser une puissance de calcul phénoménale.

---

### Complexité d'un algorithme

l'étude formelle de la quantité de ressources (par exemple de temps ou
d'espace) nécessaire à l'exécution de cet algorithme

---

### Liste a une dimention

| a | b | c | d | e | f | g | h | i |
| - | - | - | - | - | - | - | - | - |
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

- 2 est le max si et seulement si b >= a and b >= b
- 9 est le max si et seulement si i >= h

---

### Recherche linéaire

| 1 | 2 |   |   | n/2 |   |   | n-1 | n |
| - | - | - | - | -   | - | - | -   | - |
|   |   |   |   |     |   |   |     |   |


- Parcourir les pages dans l'ordre (alphabétique) jusqu'à trouver le nom cherché. |
- Le meilleur des cas est celui où le max est le premier dans la liste, le max est alors trouvé instantanément. |
- Le pire des cas est celui où le nom est le dernier dans l'annuaire, le nom est alors trouvé après avoir parcouru tous les noms |

---

### Recherche dichotomique : diviser et concquerir

ouvrir l'annuaire au milieu, si le nom qui s'y trouve est plus loin
alphabétiquement que le nom cherché, regarder avant, sinon, regarder après.
Refaire l'opération qui consiste à couper les demi-annuaires (puis les quarts
d'annuaires, puis les huitièmes d'annuaires, etc.) jusqu'à trouver le nom
cherché.

---

### Methode 0: Recherche linéaire


---

### Recherche linéaire: exemple

Si l'annuaire contient 30 000 noms, le pire cas demandera 30 000 étapes. La
complexité dans le pire des cas de cette première méthode pour n  entrées dans
l'annuaire fourni est O(n), ça veut dire que dans le pire des cas, le temps de
calcul est de l'ordre de grandeur de n : il faut parcourir tous les n noms une
fois.

---

### Methode 1: recherche dichotomique



---

## L'algorithmique dans le projet

- Ecrit par l'etre humain, l'algorithme est traduit en instructions comprehensibles par l'ordinnateur. |
- Sa premiere fonction est d'etre comprise par un autre etre humain dans l'equipe de developpement. |
- “One of my most productive days was throwing away 1000 lines of code.” – Ken Thompson

---

## Environnement de développement

- En programmation informatique, un environnement de développement est un
  ensemble d'outils pour augmenter la productivité des programmeurs qui
  développent des logiciels |
- Il comporte un éditeur de texte destiné à la programmation, des fonctions qui
  permettent, par pression sur un bouton, de démarrer le compilateur ou
  l'éditeur de liens ainsi qu'un débogueur en ligne, qui permet d'exécuter
  ligne par ligne le programme en cours de construction. |
- Certains environnements sont dédiés à un langage de programmation en
  particulier. Il ne faut pas hesiter a tout essayer pour voir ce qui permet
  d'arriver a ses fins le plus facilement. |
- Les outils qui assistent les développeurs dans toutes les étapes de la
  réalisation du logiciel: définition, conception, programmation, test et
  maintenance. |
- Ces outils tiennent également compte des différents rôles au sein d'une
  équipe de programmation: programmeur, manager et responsable qualité

---

## Environnement de développement: outils

- toujours un éditeur de texte incorporé, avec souvent la possibilité de le
  remplacer par un autre éditeur. typiquement des fonctions de mise en évidence
  alignées avec le langage de programmation: indentation automatique des blocs
  de code, marquage des délimiteurs (parenthèses ou accolades), et mise en
  évidence des mots clés du langage par de la couleur ou des caractères gras |
- outil de création d'interface graphique. Un tel outil permet au programmeur
  de gagner un temps significatif dans la construction de l'interface graphique
  de son programme. Jusqu'à l'arrivée de la technologie Java, de tels outils
  ciblaient toujours un système d'exploitation en particulier.
- outil pour réaliser automatiquement des tests.
- outils d'analyse du code source. Par exemple un générateur de graphique qui
  permet d'obtenir le diagramme en arbre de l'utilisation d'une fonction du
  programme.
- Un outil de contrôle de versions. Un tel outil permet à plusieurs
  programmeurs de travailler simultanément sur les fichiers de code source du
  programme.

---

## Environnement de développement: languages

- Java: compile le code source en bytecode pour la JVM
- C++: compile le code source en language machine
- Visual Basic, Python, PHP: interprétés

---



---
# Syntaxe des éléments clés
## Principe d'une machine à état et universalité de Turing


---?image=assets/image/kyle-gregory-devaras.jpg

## Tips!

<br>

@fa[arrows gp-tip](Press F to go Fullscreen)

@fa[microphone gp-tip](Press S for Speaker Notes)

---?image=assets/image/kyle-gregory-devaras.jpg

## Template Features

- Code Presenting |
- Repo Source, Static Blocks, GIST |
- Custom CSS Styling |
- Slideshow Background Image |
- Slide-specific Background Images |
- Custom Logo, TOC, and Footnotes |

---?code=sample/go/server.go&lang=golang&title=Golang File

@[1,3-6](Present code found within any repo source file.)
@[8-18](Without ever leaving your slideshow.)
@[19-28](Using GitPitch code-presenting with (optional) annotations.)

---?image=assets/image/john-reign-abarintos.jpg

@title[JavaScript Block]

<p><span class="slide-title">JavaScript Block</span></p>

```javascript
// Include http module.
var http = require("http");

// Create the server. Function passed as parameter
// is called on every request made.
http.createServer(function (request, response) {
  // Attach listener on end event.  This event is
  // called when client sent, awaiting response.
  request.on("end", function () {
    // Write headers to the response.
    // HTTP 200 status, Content-Type text/plain.
    response.writeHead(200, {
      'Content-Type': 'text/plain'
    });
    // Send data and end response.
    response.end('Hello HTTP!');
  });

// Listen on the 8080 port.
}).listen(8080);
```

@[1,2](You can present code inlined within your slide markdown too.)
@[9-17](Displayed using code-syntax highlighting just like your IDE.)
@[19-20](Again, all of this without ever leaving your slideshow.)

---?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&lang=scala&title=Scala GIST

@[23](You can even present code found within any GitHub GIST.)
@[41-53](GIST source code is beautifully rendered on any slide.)
@[57-62](And code-presenting works seamlessly for GIST too, both online and offline.)

---?image=assets/image/kyle-gregory-devaras.jpg

## Template Help

- [Code Presenting](https://github.com/gitpitch/gitpitch/wiki/Code-Presenting)
  + [Repo Source](https://github.com/gitpitch/gitpitch/wiki/Code-Delimiter-Slides), [Static Blocks](https://github.com/gitpitch/gitpitch/wiki/Code-Slides), [GIST](https://github.com/gitpitch/gitpitch/wiki/GIST-Slides)
- [Custom CSS Styling](https://github.com/gitpitch/gitpitch/wiki/Slideshow-Custom-CSS)
- [Slideshow Background Image](https://github.com/gitpitch/gitpitch/wiki/Background-Setting)
- [Slide-specific Background Images](https://github.com/gitpitch/gitpitch/wiki/Image-Slides#background)
- [Custom Logo](https://github.com/gitpitch/gitpitch/wiki/Logo-Setting), [TOC](https://github.com/gitpitch/gitpitch/wiki/Table-of-Contents), and [Footnotes](https://github.com/gitpitch/gitpitch/wiki/Footnote-Setting)

---?image=assets/image/kyle-gregory-devaras.jpg

## Go GitPitch Pro!

<br>
<div class="left">
    <i class="fa fa-user-secret fa-5x" aria-hidden="true"> </i><br>
    <a href="https://gitpitch.com/pro-features" class="pro-link">
    More details here.</a>
</div>
<div class="right">
    <ul>
        <li>Private Repos</li>
        <li>Private URLs</li>
        <li>Password-Protection</li>
        <li>Image Opacity</li>
        <li>SVG Image Support</li>
    </ul>
</div>

---?image=assets/image/kyle-gregory-devaras.jpg

### Questions?

<br>

@fa[twitter gp-contact](@gitpitch)

@fa[github gp-contact](gitpitch)

@fa[medium gp-contact](@gitpitch)

---?image=assets/image/gitpitch-audience.jpg

@title[Download this Template!]

### Get your presentation started!
### [Download this template @fa[external-link gp-download]](https://gitpitch.com/template/download/space)

# Formation Algorithmique

### Introduction
---
