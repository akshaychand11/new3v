if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sahidmalik07/verify2.git /verify2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /verify2
fi
cd /verify2
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py
