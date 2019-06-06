A Hat in Time's Ultrawide Issue
===

A Hat in Time has an issue with how it deals with Ultrawide resolutions. The majority of the issue is caused by how UE4 decides to deal with wider resolutions.

UE4 by default uses a method called `Vert-` (vertical minus). `Vert-`'s goal is to maintain how wide the image can be. The wider the image gets, the more it starts cropping from the top and bottom. This can be seen in the comparison shots.

The recommended method to use is `Hor+` (horizontal plus). `Hor+` instead tries to maintain how tall the image can be. This allows wider monitors to show more on the sides of the screen.

Googling `Unreal Engine 4 hor+` will bring up lots of talk of other games that have this issue.

Comparison
===

For the comparison shots, a modded exe was used for `Hor+` images.

Main Menu (May 19th update)
---

16:9 - Game Default ![alt text](/images/mainmenu_widescreen_default.png "16:9 - Game Default")

21:9 - Game Default ![alt text](/images/mainmenu_ultrawide_default.png "21:9 - Game Default")

21:9 - Modded EXE ![alt text](/images/mainmenu_ultrawide_modded.png "21:9 - Modded EXE")

The first thing I want to point out is how `21:9 - Game Default` looks like a direct cropped image of `16:9 - Game Default`. The most noticeable things I can point out is BowKid's button is no longer visible and the Main Menu's UI is cut off making it impossible to access the game's settings.

With `21:9 - Modded EXE` BowKid is now just as visible as she is in `16:9 - Game Default`, we can see the button now!

The UI cropping was patched with the [May 15th update](https://steamdb.info/patchnotes/3827253/).

The Empress' Introduction Cutscene
---

16:9 - Game Default ![alt text](/images/cutscene_widescreen_default.png "16:9 - Game Default")

21:9 - Game Default ![alt text](/images/cutscene_ultrawide_default.png "21:9 - Game Default")

21:9 - Modded EXE ![alt text](/images/cutscene_ultrawide_modded.png "21:9 - Modded EXE")

The first thing to notice is with `21:9 - Game Default`, you can only see the top of BowKid's head in the cutscene. She's simply too short to fit into the frame!

The graffiti is also shows a noticeable difference:

* In `16:9 - Game Default`, you can see there's 3 pieces of graffiti with 2 of them being cut off in the shot.
* In `21:9 - Game Default`, you can only see the pawprint and some cut off scribbles.
* In `21:9 - Modded EXE`, you can see the 3 pieces of graffiti without them being cut off to the side.

Videos
---
16:9 - Game Default

[![IMAGE ALT TEXT](http://img.youtube.com/vi/KulkCkPYdVo/0.jpg)](http://www.youtube.com/watch?v=KulkCkPYdVo "Video Title")

21:9 - Game Default

[![IMAGE ALT TEXT](http://img.youtube.com/vi/_UyjUX5YEhI/0.jpg)](http://www.youtube.com/watch?v=_UyjUX5YEhI "Video Title")

21:9 - Modded EXE

[![IMAGE ALT TEXT](http://img.youtube.com/vi/yKnb2C6C7xY/0.jpg)](http://www.youtube.com/watch?v=yKnb2C6C7xY "Video Title")

21:9 - Game Default vs Modded EXE cutscene

[![IMAGE ALT TEXT](http://img.youtube.com/vi/Ke1TzseQbUk/0.jpg)](http://www.youtube.com/watch?v=Ke1TzseQbUk "Video Title")

Console Commands used in the videos:

```
EnableCheats
Open DLC_Metro
```

An interesting side effect of `Open DLC_Metro` is if you start with a character with no time pieces, it will spawn you in the Yellow Overpass Manhole while a character with 3 timepieces spawns in the Bluefin tunnel.

Other Issues
===

Loading Screens
---

Loading screen images doesn't fill the whole screen revealing the scene behind it. Initially the loading image will pop up with the scene visible from the sides, then the scene is unloaded and a red background fills in the void.

The common solution some games use for this is the `Vert-` method to ensure the 16:9 image fills wider screens. The downside is the top and bottom is removed and the image is zoomed in making the image look lower quality. Some games from AAA studios tend to not do anything and leave the unfilled gaps with a black background.

Loading image with scene loaded ![alt text](/images/loading1.png)
Loading image with scene unloaded ![alt text](/images/loading2.png)

Chapter Map
---

With the modded EXE, the Chapter Map's UI doesn't properly align with the planet.

![alt text](/images/chaptermap_modded.jpg)

Modded EXE
===

I've added the modded exe used for the comparison shots. The exe was modded to use `Hor+` instead of `Vert-`. It can be placed in `\steamapps\common\HatinTime\Binaries\Win64\` and renamed to `HatinTimeGame.exe`.

The modded exe was modified from the [June 6th update](https://steamcommunity.com/games/AHatinTime/announcements/detail/1599255098314218849). This exe will become outdated when the game receives an update.

The images were originally taken with a modded exe from [May 11th update](https://steamcommunity.com/games/AHatinTime/announcements/detail/1609385662082175714). This exe has been placed into `/May 11th binaries/`.

The modded exe can be made with a HEX editor like HxD to change the bytes `61 0B 36 3B` to `61 0B 66 3B`.

I've written a python script called `patch.py` which can generate the modded exe. To use, place in the `HatinTime\Binaries\Win64\` directory and run it. Written under python3, untested on python2.

I came across these bytes as a solution suggested on WSGF: http://www.wsgf.org/dr/hat-time/en

Suggested Fix
===

I personally do not have any experience with Unreal Engine development, so I cant say for sure this is the correct fix, but searching around lead me to this answer:

```
Go into your project's config folder and add this to the end of the DefaultEngine.ini file

[/Script/Engine.LocalPlayer]

AspectRatioAxisConstraint=AspectRatio_MaintainYFOV
```

https://answers.unrealengine.com/questions/747293/change-engine-aspect-ratio-scaling-from-vert-to-ho.html

Personal request:
---

Add a way to disable the cinematic bars in cutscenes, Ultrawide is a popular cinematic ratio, we don't need *extra* levels of cinematography.