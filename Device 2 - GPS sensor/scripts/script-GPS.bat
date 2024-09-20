
adb shell am start -n "com.sample.foo.simplelocationapp/com.sample.foo.simplelocationapp.MainActivity" -a android.intent.action.MAIN -c android.intent.category.LAUNCHER
echo WScript.Sleep^(WScript.Arguments^(0^)^) >"%temp%sleep.vbs" && cscript "%temp%sleep.vbs" 1000 >nul
adb shell am startservice com.quicinc.trepn/.TrepnService
echo WScript.Sleep^(WScript.Arguments^(0^)^) >"%temp%sleep.vbs" && cscript "%temp%sleep.vbs" 1000 >nul
adb shell am broadcast -a com.quicinc.trepn.load_preferences -e com.quicinc.trepn.load_preferences_file "hadas_preferences.pref"
echo WScript.Sleep^(WScript.Arguments^(0^)^) >"%temp%sleep.vbs" && cscript "%temp%sleep.vbs" 1000 >nul
adb shell am broadcast -a com.quicinc.trepn.start_profiling -e com.quicinc.trepn.database_file "longPolling.db"
echo WScript.Sleep^(WScript.Arguments^(0^)^) >"%temp%sleep.vbs" && cscript "%temp%sleep.vbs" 60000 >nul
adb shell am broadcast -a com.quicinc.trepn.stop_profiling
adb shell am broadcast -a com.quicinc.trepn.export_to_csv -e com.quicinc.trepn.export_db_input_file "longPolling.db" -e com.quicinc.trepn.export_csv_output_file "lp30005000.csv"
echo WScript.Sleep^(WScript.Arguments^(0^)^) >"%temp%sleep.vbs" && cscript "%temp%sleep.vbs" 3000 >nul
adb pull /storage/emulated/0/trepn/lp30005000.csv
adb shell rm /storage/emulated/0/trepn/lp30005000.csv
adb shell rm /storage/emulated/0/trepn/longPolling.db


adb shell am force-stop com.sample.foo.simplelocationapp


exit