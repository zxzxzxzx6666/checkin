$.getJSON("/announce_card", function(rawdata){
    // 取出所有資料
    data = rawdata.data;
    // 將資料一行一行寫到網頁
    row1 = data[0];
    row2 = data[1];
    // 呼應到網頁的 class = announcemain
    $('.cardname01').append(row1[0]);
    $('.cardvalue01').append(row2[0]);
    $('.cardname02').append(row1[1]);
    $('.cardvalue02').append(row2[1]);
    $('.cardname03').append(row1[2]);
    $('.cardvalue03').append(row2[2]);
    $('.cardname04').append(row1[3]);
    $('.cardvalue04').append(row2[3]);
    $('.cardname05').append(row1[4]);
    $('.cardvalue05').append(row2[4]);
    $('.cardname06').append(row1[5]);
    $('.cardvalue06').append(row2[5]);
    $('.cardname07').append(row1[6]);
    $('.cardvalue07').append(row2[6]);
    $('.cardname08').append(row1[7]);
    $('.cardvalue08').append(row2[7]);
});