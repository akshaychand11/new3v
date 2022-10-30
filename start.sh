if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sahidmalik07/verify-repo.git /verify-repo
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /verify-repo
fi
cd /verify-repo
pip3 install -U -r requirements.txt
echo "Starting Bot....💥"
python3 bot.py
