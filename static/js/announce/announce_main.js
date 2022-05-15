$.getJSON("/announce_main", function(rawdata){
    // 取出所有資料
    data = rawdata.data;
    console.log(data)
    // 將資料一行一行寫到網頁
    for (let i = 0; i < 6; i++) {
        row = data[i];
        if (row) {
        // 呼應到網頁的 class = announcemain
        $('.announcemain').append(
        '<tr>'
            +'<td>'+row[1]+'</td>'
            +'<td>'
                //根據id給定超連結
                +'<a href = /announceContent/'+row[0]+'>'
                    +row[2]
                +'</a>'
            +'</td>'
            +'<td>'+row[3]+'</td>'
            +'<td>'+row[4]+'</td>'
        +'</tr>');
        }
    }
});