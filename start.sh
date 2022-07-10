if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sahidmalik07/movies-house-bot.git /movies-house-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /movies-house-bot
fi
cd /movies-house-bot
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py
