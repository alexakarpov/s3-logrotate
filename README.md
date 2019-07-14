A brain dead script to accompany the script from here:
https://www.mkyong.com/linux/linux-script-to-backup-mysql-to-amazon-s3/

basically, as you add the script ^ to your crontab, add somethink like this line to that script:

Usage:

**python3 ~/logrotate.py <your_bucket_name> <prefix_to_your_backups> <max_number_of_files_to_keep>**
