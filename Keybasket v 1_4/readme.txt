
Readme for Keybasket v 1.4.2
MIT License

@author Andrew Vella
productionsofthemathbunny@gmail.com
 
________________________

Contents

Start
License
Introduction
Features
Detailed Features
Errors (Error Handling)
Restoring the Application
Contents of Sample

________________________

Start

To start this application run GUI_main in Keybasket_src

You can run it with IDLE or the IDE of your choice without issue.

If you like to run this app from the shell (terminal) you can do so.
However, you should do so from the directory Keybasket_src
The shell and tkinter do not get along, and it will activate the restore procedure.

If you click yes, the restore will fail, nothing will change.
If you click no, you will get ErrCode 3 (files erased). No files have been erased.
I do not know why this happens 

Use 'cd' to access it
Use 'python3 ./ GUI_main.py' to run it
Do not include quotes

________________________

MIT License

Copyright (c) 2020 Andrew Jones Vella

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

________________________


Introduction

Hello, I am glad you are taking the time to read this. Welcome to Keybasket, developed by Andrew Vella.

If you have any questions you can email me at:
productionsofthemathbunny@gmail.com

Keybasket is an application that takes the mental gymnastics of
password creation. You create a list of keywords for yourself.
Keybasket will happily stitch them together into string with 
numbers and symbols. I need not reiterate the About message here!

The current version of this application requires that you install python3. The link to install that is here:

https://www.python.org/downloads/

I know it's widely understood that an app would be nicely bundled for you with an icon and run all on its own. That would be very nice indeed, and I am working on that! That said, I call this an application because it is a program that has applications.

________________________

Features

The features of the application are as follows:

Generate Account Names: Generates 50 account names with selected file
Generate Passwords: Generates 50 passwords with selected file
Hash Key: Produces a pseudo-random 72 character hash based on a keyword
Two Key Hash: Produces a pseudo-random 72 char hash based on 2 keywords

Select File: Use to select a file for the generate features
Create File: Create a file
Update File: Modify the contents of the selected file

Files with invalid characters will not be workable
Avoid punctuation, dashes, and spaces. You can use underscores  ' _ '

________________________


Detailed Features

It is not explicitly necessary to describe every feature of the app in detail here, but I will describe some of the more esoteric ones.

-Deleting a File-
	
If you would like to delete a file, click on Update File and erase its contents. The next time the application starts, the file will be marked for deletion. If the file is still empty when you close the main window, the marked file will be deleted.

-Hashing-

Keybasket includes a hashing feature designed to eliminate the need to memorize or store passwords. It is simpler to remember a word or name.

The hash is pseudo-random such that any key you give will always produce the same hash. You can then use this hash as a password.

E.g.

1234

82z'f2mT:b\\GQ3\\:!d60x%d0kR8tnYcEnL3v_YDN0Y7\{aUO:D&O-qWKE0:yE#gMGA,6uA|cI {mgR\>gE,o}

For a little extra security you can use the two key hash, but if your second key does not produce a secure hash with the first, it will be updated. A secure key contains at least 8 distinct characters with no repeating characters

If you are so inclined you can even do this for each password you need:
	
	KEY 1	KEY 2

	1234	Facebook

	1234	Twitter

	1234 	Youtube

	1234	1234567890

That said, avoid common passwords like 1234, or password, these are never a secure options.

I choose them because choosing a more secure key would render that key less secure. If you use 1234 with the one key hash for a password. Then, your password is currently listed above. Do not do that.

-Conversion-

Files are converted to the extension .bin when not in use by the application. They cannot be modified unless they are converted back to text.

________________________

Errors (Error Handling)

There are eight errors this application will throw:

An Error Occurred. (ErrCode 0)

Missing reference for file. (ErrCode 1)

File Not Found. (ErrCode 2)

Critical Files Erased. (ErrCode 3)

Critical File Not Found. (ErrCode 4)

An Operation Could Not Be Completed. (ErrCode 5)

Close down procedure failure. Restart the application to resolve it. (Errcode 6)

Restore Failure; The Application has been tampered with. The restore file has been compromised. (ErrCode 7)

________________________


Restoring the Application

The Restore Procedure starts up when the application cannot function because critical files are missing, cannot be found, or cannot be referred to. 

The two critical files are Sample and Files. Keybasket cannot operate without them.

Sample contains over 1000 names to use with the application. It is the default file to use.

Files contains the names of other files in the Words directory. It keeps track of how many files there are and what they are called. If a file name is removed from Files, it will be assumed to not exist. Any file not listed in Files is delete during file verification at start-up and close-down

Restoring the application erases the contents of the Words directory and all of the files it contains (that is to say, all the files you have created while using the program). Then an empty Words directory is created and populated with a copy of Sample from the Backup directory
and a Files file. Files contains only the word Sample, referring to the Sample file.

You will be asked if you would like to restore the application until you restore it.
If you want to keep these files, copy them and save them somewhere else.

Please enjoy Keybasket, I hope you will find it useful.

________________________


Contents of Sample

8D
APMBE
Abbey
Abbie
Abby
Abel
Abigail
Abreu
Ace
Adam
Addie
Admiral
Aeolian
Aggie
Aires
Album
Aldo
Alef
Alex
Alexis
Allie
Ally
Amber
Amie
Amigop
Amos
Amy
And
Anderson
Andrew
Andy
Angel
Angus
Anime
Annie
Anthem
Apollo
April
Archie
Architect
Argus
Aries
Arithmetic
Arm
Armanti
Arnie
Arrow
Art
Asclepius
Ashes
Ashley
Astro
Athena
Atlas
Audi
Augie
Aussie
Austin
Autumn
Avian
Avyen
Axel
Axle
Babbles
Babe
Baby
Baby_Doll
Babykins
Bacchus
Bailey
Bam_Bam
Bambi
Bandit
Banjo
Barbie
Barclay
Barker
Barkley
Barley
Barnaby
Barney
Baron
Bart
Basil
Basket
Baxter
Bb
Be
Beamer
Beanie
Beans
Bear
Beau
Beauty
Beaux
Bebe
Beetle
Bell
Bella
Belle
Beller
Ben
Benji
Benny
Benson
Bentley
Bernie
Berry
Bessie
Biablo
Bibbles
Bigboy
Bigfoot
Biggie
Billie
Billy
Bingo
Binky
Birdie
Birdy
Biscuit
Bishop
Bits
Bitsy
Bizzy
Black_Jack
Blanche
Blast
Blaze
Blitzen
Blondie
Bloomer
Blossom
Blue
Bo
Boa
Bob
Bobbie
Bobby
Bobo
Bodie
Bogey
Bones
Bongo
Bonnie
Boo
Boo_Boo
Booker
Boone
Booster
Bootie
Boots
Boris
Bosco
Bosley
Boss
Bowie
Boy
Bozley
Bradley
Brady
Braggs
Brandi
Brando
Brandy
Bravo
Bridgett
Bridgette
Brie
Brindle
Bringas
Brit
Brittany
Brodie
Brook
Brooke
Brownie
Bruiser
Bruno
Brutus
Bubba
Bubbles
Buck
Buckeye
Bucko
Bucky
Bud
Buddha
Buddie
Buddy
Buddyboy
Buffie
Buffy
Bug
Bugsey
Bugsy
Bullet
Bullet_Time
Bullet_Time_Fighting
Bullwinkle
Bully
Bumper
Bunky
Bunny
Burton
Buster
Buster_Brown
Butch
Butchy
Butter
Butterball
Buttercup
Butterscotch
Buttons
Buzzy
C
Caesar
Cali
Callie
Calvin
Cameo
Camille
Candy
Capone
Captain
Carley
Carlin
Casey
Casper
Cassie
Cassis
Cell
Central
Chacha
Chad
Chamberlain
Champ
Chance
Chanel
Chaos
Charisma
Charles
Charlie
Charliebrown
Charmer
Chase
Chauncey
Chaz
Checkers
Chelsea
Chessie
Chester
Chevy
Chewie
Chewy
Cheyenne
Chic
Chichi
Chico
Chief
Chili
China
Chip
Chipper
Chippy
Chips
Chiquita
Chivas
Chloe
Chocolate
Chrissy
Chubbs
Chucky
Chyna
Ciliate
Cinder
Cindy
Cinnamon
Cisco
Claire
Clancy
Cleo
Cleopatra
Clicker
Clifford
Clojure
Clover
Clyde
Coal
Cobweb
Coco
Cocoa
Coconut
Codi
Cody
Cola
Cole
Colton
Comet
Commando
Compiler
Conan
Connor
Cookie
Cooper
Copper
Copyright
Corky
Corntooh
Corntooth
Cosmo
Cotton
Cozmo
Crackers
Cricket
Crossroad
Crossword
Crystal
Cubby
Cubs
Cujo
Cupcake
Cupid
Curly
Curry
Cutie
Cutie_Pie
Cyrus
Daddy
Daffy
Daisey_Mae
Daisy
Dakota
Dali
Dallas
Dan
Dancer
Danny
Dante
Daphne
Darby
Darcy
Darwin
Dash
Dasher
Dave
Dayo
Deacon
Dee
Deedee
Dempsey
Dennis
Dennis_Gid
Destini
Dewey
Dexter
Dharma
Diamond
Diana
Dianna
Dickens
Diego
Diesel
Dillon
Dinky
Dino
Diva
Dobie
Doc
Dodger
Doggon
Dolly
Domino
Donnor
Doodles
Doogie
Dorian
Dots
Dottie
Dozer
Dracula
Dragon
Dragster
Dreamer
Drumph
Duchess
Dude
Dudley
Duffy
Dufour
Duke
Duncan
Dung
Dunn
Dusty
Dutches
Dutchess
Dylan
Earl
Ebony
Echo
Eckmann
Eddie
Eddy
Edgar
Edsel
Eifel
Einstein
Ellie
Elliot
Elmo
Elvis
Elwood
Ember
Emerald
Emily
Emma
Emmy
Erin
Ernie
Eva
Faith
Fancy
Farter
Feces
Feist
Felix
Fergie
Ferris
Fido
Fifi
Figaro
Fingertips
Finnegan
Fiona
Flake
Flakey
Flansburgh
Flash
Flint
Flood
Flower
Floyd
Fluffy
Flute
Fonzie
Foxy
Francais
Frankie
Franky
Freckles
Fred
Freddie
Freddy
Freedom
Freeway
Fresier
Friday
Frisco
Frisky
Fritz
Frodo
Frosty
Furball
Fuzzy
Gabby
Gabriella
Galaga
Galumph
Gamete
Garfield
Gasby
Gaseous
Gates
Gator
Gavin
Gene
Generic
Genie
George
Georgia
Georgie
Giant
Giants
Gibson
Gid
Gidget
Gigi
Gilbert
Gilda
Gina
Ginger
Ginny
Girl
Gizmo
Glean
Gobble
Godiva
Gogol
Goku
Goldie
Goober
Goomph
Goop
Goose
Gordon
Grace
Gracie
Grady
Grant
Green
Greenie
Greta
Gretchen
Gretel
Gretta
Griffen
Grinch
Grizzly
Gromit
Grover
Grue
Gucci
Guinness
Gunner
Gunther
Gurt
Gus
Guy
Hailey
Hal
Haley
Hallie
Hamlet
Hammer
Hank
Hanna
Hannah
Hans
Happy
Hardy
Harley
Harpo
Harrison
Harry
Hart
Harvey
Heather
Heidi
Henry
Hercules
Hershey
Higgins
Hiway
Hobbes
Hodges
Holly
Homer
Honey
Honey_Bear
Hoover
Hope
Houdini
House
Howie
Hudson
Huey
Hugh
Hugo
Huh
Humour
Humphrey
Hunter
Hydra
India
Indy
Infringement
Instant
Ionian
Iris
Isabella
Isabelle
Itsy
Itsy_Bitsy
Ivory
Ivy
Izzy
Jack
Jackie
Jackpot
Jackson
Jade
Jagger
Jags
Jaguar
Jake
Jamie
Jasmine
Jasper
Java
Jaxson
Jazmie
Jazz
Jelly
Jelly_Bean
Jenna
Jenny
Jerry
Jersey
Jess
Jesse
Jessejames
Jessie
Jest
Jester
Jesus
Jet
Jethro
Jett
Jetta
Jewel
Jewels
Jim
Jimmuy
Jingles
Jj
Jobs
Joe
Joey
John
Johnny
Jojo
Joker
Jolie
Jolly
Jones
Jordan
Josie
Jost
Joy
Judy
Julius
June
Junior
Justice
Kali
Kallie
Kamehameha
Kane
Karma
Kasey
Katie
Kato
Katz
Kayla
Kc
Keesha
Kellie
Kelly
Kelsey
Kenya
Kerry
Kettles
Keybasket
Keyseed
Kibbles
Kid
Kiki
Killian
King
Kipper
Kira
Kirby
Kismet
Kissy
Kitsune
Kittothenes
Kitty
Kiwi
Klaus
Koba
Kobe
Koda
Koko
Kona
Kosmo
Koty
Kramer
Kravsky
Kujo
Kurly
Kyra
Lacey
Laddie
Ladeda
Lady
Ladybug
Lamby
Land
Laney
Lassie
Latte
Layla
Lazarus
Lee
Lefty
Lehrer
Lennon
Leo
Levi
Lexeme
Lexi
Lexie
Lexus
Libby
Lightning
Lili
Lilly
Lily
Lincoln
Linnel
Linus
Lisp
Little_Guy
Little_One
Little_Rascal
Littlebit
Lizzy
Logan
Logic
Loki
Lola
Lorena
Lou
Louie
Louis
Love
Lovey
Lucas
Luci
Lucky
Lucy
Luke
Lulu
Lumberland
Luna
Lynx
Mac
Macho
Macintosh
Mack
Mackenzie
Macy
Maddie
Maddy
Madison
Maggie
Maggie_Mae
Maggie_Moo
Maggy
Magic
Magnolia
Majin
Major
Mandi
Mandy
Mango
Marble
Mariah
Marley
Marty
Mary
Maryjane
Mason
Math
Math_Bunny
Matrix
Mattie
Maverick
Max
Maximus
Maxine
Maxwell
May
Maya
McCartney
Mckenzie
Mcquade
Meadow
Megan
Meggie
Mercedes
Mercle
Merlin
Mia
Miasy
Michael
Mickey
Microcosmo
Midnight
Might
Mikey
Miko
Miles
Miller
Millie
Milo
Mimi
Mindy
Ming
Mini
Minnie
Mischief
Misha
Missie
Missy
Mister
Misty
Mitch
Mittens
Mitzi
Mitzy
Mo
Mocha
Mojo
Mollie
Molly
Mona
Monk
Monster
Montana
Montgomery
Monty
Mookie
Moonshine
Moose
Morgan
Morph
Moses
Mouse
Muffin
Mugsy
Mulligan
Munchkin
Murphy
NEOWISE
Nakita
Nala
Name
Nana
Nand
Nanobots
Natasha
Nathan
Nebula
Nellie
Nemo
Nena
Neo
Nero
Nestle
Neutron
Newt
Newton
Nibbles
Nibby
Nibby_Nose
Nick
Nickers
Nickie
Nicky
Nico
Nike
Niki
Nikita
Nikki
Niko
Nina
Nipton
Nitro
Nobel
Noel
Nona
Noname
Noodles
Nor
Norton
Nosey
Not
Nugget
Nutmeg
Oakley
Obie
Odie
Oldglory
Olive
Oliver
Olivia
Ollie
One
Onie
Onyx
Opie
Or
Orange
Oreo
Oscar
Otis
Otto
Owl
Oz
Ozwalt
Ozzie
Ozzy
Pablo
Paco
Paddington
Paddy
Pancakes
Panda
Pandora
Panther
Papa
Paris
Parker
Parser
Pasha
Pasta
Patch
Patches
Patricky
Patty
Peaches
Peanut
Peanuts
Pearl
Pebbles
Pedro
Penny
Pepper
Peppy
Pepsi
Persy
Pertness
Pete
Peter
Petey
Petie
Phantom
Phoebe
Phoenix
Piano
Picasso
Pickit
Pickles
Pie
Pierre
Pigeon
Piggy
Piglet
Pink
Pinkpanther
Pinky
Pinto
Pip_Squeek
Piper
Pippin
Pippy
Pirate
Pixie
Plato
Pluto
Pockets
Pogo
Pokey
Polly
Poncho
Pongo
Pooch
Poochie
Pooh
Pooh_Bear
Pookie
Pooky
Poop
Popcorn
Poppy
Porche
Porkchop
Porky
Porter
Poseidon 
Powder
Prancer
Prasad
Precious
Presley
Pretty
Prince
Princess
Prior
Priss
Prissy
Processing
Productions
Pryor
Puddles
Pudge
Puffy
Pugsley
Pumpkin
Punkin
Puppy
Purdy
Python
Qu
Queen
Queenie
Questionable
Quincy
Quinn
Rags
Raison
Ralph
Ralphie
Rambler
Rambo
Ranger
Rascal
Raven
Read
Rebel
Red
Reggie
Reilly
Remix
Remy
Rex
Rexy
Rhett
Ricky
Rico
Riggs
Riley
Ringo
Rintintin
Ripley
Robot
Robots
Rocco
Rock
Rocket
Rocko
Rocky
Roland
Rolex
Rollie
Roman
Romeo
Rosa
Roscoe
Rosebud
Rosie
Rosy
Rotifer
Rover
Rowdy
Roxanne
Roxie
Roxy
Ruby
Ruchus
Rudolph
Rudy
Ruffe
Ruffer
Ruffles
Rufus
Ruger
Rusk
Rusty
Ruthie
Ryder
Sabine
Sable
Sabrina
Sadie
Sage
Sailor
Saitama
Saiyan
Salem
Sally
Salty
Sam
Samantha
Sammy
Sampson
Samson
Sandwich
Sandy
Santana
Sara
Sarah
Sarge
Sasha
Sassie
Sassy
Savannah
Sawyer
Scarlett
Scheme
Schotzie
Schultz
Scoobert
Scooby
Scooby_Doo
Scooter
Scottie
Scout
Scrappy
Scratch
Scruffy
Sea
Sebastian
Seth
Shadow
Shady
Shaggy
Shasta
Sheba
Sheena
Sheep
Shelby
Shelly
Sherman
Shiloh
Shiner
Shorty
Sidharth
Sienna
Sierra
Silky
Silver
Silvester
Simbort
Simon
Simone
Sixty_Four
Skeeter
Skinny
Skip
Skipper
Skippy
Sky
Skye
Skyler
Slick
Slinky
Sly
Smarty
Smith
Smoke
Smokey
Smudge
Sneakers
Snickers
Snoop
Snoopy
Snowball
Snowflake
Snowy
Snuffles
Snuggles
So
Soand
Soap
Socks
Solomon
Sonny
Sophia
Sophie
Spanky
Sparkle
Sparky
Specs
Spectacles
Speed
Speediest
Speedy
Spencer
Spider
Spike
Spirit
Spirochete
Sponge
Spot
Spotty
Spud
Spunky
Squeeky
Squirt
Stanley
Star
Starfish
Starr
Stella
Sterling
Stich
Stinky
Stormy
Stuart
Sturm
Sugar
Sugar_Baby
Summer
Sumo
Sundance
Sunday
Sunny
Sunshine
Susie
Susie_Q
Suzy
Sweet_Pea
Sweetie
Sweetie_Pie
Sydney
T_Bird
T_Bone
Tabby
Tabetha
Taco
Taffy
Tally
Tammy
Tangerine
Tangles
Tango
Tank
Tanner
Tara
Tasha
Taylor
Taz
Teddy
Teddy_Bear
Tedone
Tequila
Tess
Tessa
Tessie
Tex
The
Thelma
Them
They
Thinkerbelly
Thor
Thumb
Thunder
Thyme
Tiffany
Tiger
Tiggy
Tiki
Tilly
Timber
Timmy
Tinker
Tinky
Tiny
Tippy
Tipr
Titan
Tito
Titus
Tobie
Toby
Toddler
Toffee
Token
Tom
Tom_Seven
Tommy
Tommy_Boy
Toni
Tony
Toot
Toots
Topaz
Tori
Toto
Tracker
Tramp
Transmission
Trapper
Travis
Trigon
Trinity
Tripod
Tristan
Trixie
Trooper
Trouble
Troy
Truffles
Tuck
Tucker
Tuesday
Tuffy
Turbo
Turner
Tux
Twiggy
Twinkle
Ty
Tyler
Typhoon
Udo
Uiopas
Uname
Unamed
Unbelievable
Undecided
Underpants
Underwear
Underwhere
Unit
Unmakes
Unmakinator
Untitled
Urine
Urinetown
Uruguay
Uterus
Uva
Uvula
Valinto
Vampire
Vava
Vegas
Velvet
Vinnie
Vinny
Violet
Violin
Viscardi
Vishnu
Vito
Volvo
Vorpal
Waffles
Wagon
Waldo
Wallace
Wally
Walter
Wayne
Weaver
Webster
Weinkauf
Weschler
Wesley
Westie
Whiskers
Whiskey
Whispy
Whiz
Wiggles
Wilber
Willie
Willow
Willy
Wilson
Winnie
Winston
Winter
Wise
Wiz
Wizard
Wolf
Wolfgang
Wolfie
Womxn
Wonder
Woody
Woofie
Wow
Wrigley
Wrinkles
Wyatt
Xena
Xevious
Xkey
Xor
Xray
Xtreme
Xylophone
Yaka
Yang
Yeller
Yellow
Yin
Yogi
Yogurt
Yukon
Zack
Zeke
Zena
Zeus
Ziggy
Zippy
Zoe
Zoey
Zoie
Zork
Zorro