from LuckyX.core.bot import Lucky
from LuckyX.core.dir import dirr
from LuckyX.core.git import git
from LuckyX.core.userbot import Userbot
from LuckyX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Lucky()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
