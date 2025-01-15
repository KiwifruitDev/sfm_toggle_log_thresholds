# SFM Toggle Log Thresholds Script
Stop SFM from deleting redundant keys automatically!

This script toggles the "Log Threshold" system that SFM uses internally to decide similarity are when trying to delete "redundant" keyframes.

It's useful if you're working on very complex animation in the motion editor, as otherwise SFM may "compress" the samples which may change your desired animation.

Optionally, install [Autoinit Manager](https://steamcommunity.com/sharedfiles/filedetails/?id=3400621327) to automatically disable them on startup.

SFM will automatically run the redundant keyframe deletion when loading a session without first disabling the thresholds, so you should definitely install [b]Autoinit Manager[/b] to make sure you don't lose your work.

## Usage
Perform the following steps to use this script:
- (Optional) Install [Autoinit Manager](https://steamcommunity.com/sharedfiles/filedetails/?id=3400621327).
- Install this script from the Workshop.
- Once SFM has updated the Workshop items, restart SFM.
- If [b]Autoinit Manager[/b] was installed, no more action is needed.
- Otherwise, open the "Scripts" menu in the toolbar of SFM and navigate through "kiwifruitdev" and click "toggle log thresholds".
- This will toggle on or off and show a message box indicating the current state of the thresholds.

## Development
If you are a developer, check out this script on [GitHub](https://github.com/KiwifruitDev/sfm_toggle_log_thresholds).

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Funding
If you would like to support my work, you can check out [Nonsensical Video Generator](https://store.steampowered.com/app/2516360/Nonsensical_Video_Generator/), buy me a coffee on [Ko-fi](https://ko-fi.com/kiwifruitdev), become a sponsor through [GitHub Sponsors](https://github.com/sponsors/KiwifruitDev), or simply share my scripts with others. Thank you for your support!
