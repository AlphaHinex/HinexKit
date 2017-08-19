for i in {1..2000}
do
    curl 'http://best.zhaopin.com/API/ScoreCompany.ashx' -H 'Referer: http://best.zhaopin.com/' --data 'bestid=1093&score=5%2C5%2C5%2C5%2C5%2C5'
    sleep $(($RANDOM%5))
    if [[ $(($RANDOM%10)) > 3 ]]; then
        curl 'http://best.zhaopin.com/API/Vote.ashx' -H 'Referer: http://best.zhaopin.com/' --data 'bestid=1093'
        sleep $(($RANDOM%5))
    fi
done
