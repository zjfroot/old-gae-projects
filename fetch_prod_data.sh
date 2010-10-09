appcfg.py download_data --application=fan-yi --url=http://fan-yi.appspot.com/remote_api --filename=production_data 
appcfg.py upload_data --application=fan-yi --filename=production_data --url=http://localhost:10001/remote_api fanyi/
rm bulkloader*
