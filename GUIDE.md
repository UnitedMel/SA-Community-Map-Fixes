<h1 align="center">SA Modding for Dummies</h1>

**SA Modding for Dummies** is a simple modding guide that will quickly teach you how to install mods on GTA San Andreas.

# Glossary:
- **gamedir** — The main directory where the GTA executable file is located.

# Utilities:

## [Various GTA Downgraders](http://downgraders.rockstarvision.com/)
**Restores removed music and your beloved Hot Coffee minigame.**
## Installation:
> *As an alternative, just find a clean copy of 1.0 SA*

**RGSC to 1.0**
- Extract to **gamedir**
- Run **install.bat** and wait until window disappears.
- Launch via **GTA-sa.exe** and **not** RGSC launcher.

**Steam to 1.0**
- Extract to **gamedir**
- Run **install.bat** and wait until window disappears.
- Launch via **GTA-sa.exe**

## [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases)
**Adds ASI plugin loading functionality.**
## Installation:
> *Download Ultimate-ASI-Loader.zip*

- Extract **dinput8.dll** to **gamedir**
- Remove existing **vorbisFile.dll**
- Rename ```dinput8.dll``` to ```vorbisFile.dll```

## [PortableGTA](http://gta.rockstarvision.com/workshop/portablegta.dll)
> *If the link does not work, manually copy and paste it into the search bar.*

**Makes III/VC/SA use gamedir/userfiles for saves and settings instead of Documents/GTA User Files.**
## Installation:
- Create **scripts** folder in **gamedir**
- Extract **portablegta.dll** to **scripts**
- Rename ```portablegta.dll``` to ```portablegta.asi``` 
> *If you don't know how to do it, search "Enabling File Extensions".*

> *Please make sure your **gamedir** isn't Read-Only (the corresponding flag in the **gamedir** properties shouldn't be ticked).*

## [Debug Menu](https://github.com/aap/debugmenu/releases/)
**An in-game menu for III, VC and SA to tweak values and execute commands from within the game.**
## Installation:
- Extract **debugmenu.dll** from archive's "SA" folder to **gamedir**

- Download [gtadebug](https://github.com/aap/gtadebug/releases/)
- Extract **sa_debug.dll** to **scripts**
- Rename ```sa_debug.dll``` to ```sa_debug.asi```
> *Controls: CTRL+M to enable/disable menu; CTRL+B to enable/disable free camera mode, while enabled press CTRL+C to switch player control.*

## [GInput](https://cookieplmonster.github.io/mods/gta-sa/)
**Completely rewrites GTA controls handling. This way, your PS3 and Xbox 360 gamepads will be handled by the game just perfectly.**
## Installation:
- Extract **ps3btns.txd**, **sixaxis.txd**, **x360btns.txd** to **models**
- Extract **GInputSA.asi**, **GInputSA.ini** to **scripts**

## [Open Limit Adjuster](https://github.com/ThirteenAG/III.VC.SA.LimitAdjuster/releases)
**Turns whatever previously was limited into unlimited, being only limited by the machine/application capacity.**
## Installation:
- Extract **III.VC.SA.LimitAdjuster.asi**, **III.VC.SA.LimitAdjuster.ini** to **scripts**

## [CLEO4](https://github.com/cleolibrary/CLEO4/releases)
**Library plugin which brings new possibilities in scripting.**
## Installation:
- Extract **cleo** folder to **gamedir**
- Extract **bass.dll** and **CLEO.asi** to **gamedir**

## [ModLoader](https://github.com/thelink2012/modloader/releases)
**Adds an easy and user-friendly way to install and uninstall modifications into the game.**
## Installation:
- Extract all contents to **gamedir**

## *(Optional)* [Euryopa](http://aap.papnet.eu/gta/utils/librw_bin/euryopa.exe)
> *If the link does not work, manually copy and paste it into the search bar.*

**Map viewer for III/VC/SA/LCS/VCS.**
## Installation:
- Move **euryopa.exe** to **gamedir**

# Bug Fixes:

## [Widescreen Fix](https://github.com/ThirteenAG/WidescreenFixesPack/releases/tag/gtasa)
**Improves widescreen resolutions support and fixes HUD aspect ratio.**
## Installation:
- Extract **GTASA.WidescreenFix.asi**, **GTASA.WidescreenFix.ini** to **scripts**
- *(Optional)* Extract **LOADSCS.txd** to **gamedir/models/txd**
> *(Optional) [Pre-configured .ini file](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/INI.WidescreenFix.zip)*

## [SilentPatch](https://cookieplmonster.github.io/mods/gta-sa/)
**Fixes numerous bugs.**
## Installation:
- Extract **SilentPatchSA.asi**, **SilentPatchSA.ini** to **scripts**
> *(Optional) [Pre-configured .ini file](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/INI.SilentPatch.zip)*

## [Vehicle Lights Fix](https://www.dropbox.com/s/lyyays2yulz71n7/vehlightsfix.rar)
**Fixes rendering bugs of vehicle lights.**
## Installation:
- Extract **vehlightsfix.asi** to **scripts**
> *Incompatible with some Fastman Limit Adjuster's features.*

# Visuals:

## [SkyGfx](https://github.com/aap/skygfx/releases)
**Brings accurate PS2 and Xbox graphics to the PC version of San Andreas.**
## Installation:
- Extract **neo**, **stream.ini** to **gamedir**
- Extract **colorcycle.dat**, to **data**
- Extract **Mobile_details.txd**, **texdb.txt** to **models**
- Extract **skygfx.asi**, **skygfx1.ini** to **scripts**
> *(Optional) [Pre-configured .ini file](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/INI.SkyGfx.zip)*

## [SkyGrad](https://www.dropbox.com/s/e4493knjlbltptm/skygrad.rar)
**Fixes sky banding that made the gradient looking blocky.**
## Installation:
- Extract **skygrad.asi** to **scripts**

## [Project2DFX](https://github.com/ThirteenAG/III.VC.SA.IV.Project2DFX/releases/tag/gtasa)
**Adds LOD corona effect to a game map, making LOD-world look a lot better.**
## Installation:
- Extract **SALodLights.asi**, **SALodLights.ini**, **SALodLights.dat** to **scripts**
> *(Optional) [Pre-configured .ini file](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/INI.Project2DFX.zip)*

## [PC Archives Patch](https://mega.nz/file/gNlAgLIZ#cXgx5Z9-DQDD8aMMk3V0TXBhYlq8LmDQK75Zn9yAFrk)
**Optimized IMG archives including: uncompressed map textures with enabled mipmaps from III/VC/MH, restored data values and vehicle models from PS2.**
## Installation:
- Extract all contents to **gamedir**

## *(Optional)* [SkyUI](https://gtaforums.com/topic/899738-skyui/)
**Aims to bring a most accurate version of the PS2/Xbox user interface to PC.**
## Installation:
- Extract **fronten1.txd**, **hud.txd** to **models**
- Extract **text** folder contents to **text**
- Extract **skyui.asi** to **scripts**
> *Causes crash on using Trip Skip feature.*

# Map:
> *Mods are usually incompatible with each other if they use the same files and maps are no exception.*
> *Always compare the features of the same type of mods.*

## [SA Community Map Fixes](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/SA.CommunityMapFixes.zip)
> *PC Archives Patch is required.*

**Work-in-Progress compilation of map bug fixes with additional improvements.**
## Installation:
- Extract **SA Community Map Fixes** to **modloader**
- Extract **GRGX.asi**, **SAEnexLimit.asi**, **SALodLights.dat** to **scripts**
- Extract **Mobile_details.txd** to **models**

## [Vending Machine Variants](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/Tweaks.VendingVariants.zip)
> *Add-on for CMF.*

**If the default ones are boring to you.**
## Installation:
- Extract choosen folder to **modloader**

## [Classic Pickups](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/Tweaks.ClassicPickups.zip)
> *Add-on for CMF.*

**III/VC/LCS/VCS styled pickup icons.**
## Installation:
- Extract to **modloader**

## ["The Clam Digger" Billboard](https://github.com/UnitedMel/SA-Community-Map-Fixes/releases/download/latest/Tweaks.LCSBillboard.zip)
> *Add-on for CMF.*

**Unused LCS billboard. Replaces ZIP billboard in Los Santos. Looks fancy.**
## Installation:
- Extract to **modloader**
