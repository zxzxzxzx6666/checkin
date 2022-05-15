$.getJSON("/announce_main", function(rawdata){
    // 取出所有資料
    data = rawdata.data;
    id = {{id.title}};
    dataId = data[id-1];
    // 將資料一行一行寫到網頁
    console.log(data);
    console.log(dataId);
    $('.announcemain').append(
        '<tr><th>分類</th><th>'+dataId[1] +'</th></tr>'+
        '<tr><th>標題</th><th>'+dataId[2]+'</th></tr>'+
        '<tr><th>時間</th><th>'+dataId[3]+'</th></tr>'+
        '<tr><th>內容</th><th>'+dataId[4]+'</th></tr>'+
        '<tr><th>點閱</th><th>'+dataId[5]+'</th></tr>')
});