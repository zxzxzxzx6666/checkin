$.getJSON("/announce_card", function(rawdata){
    // 取出所有資料
    data = rawdata.data;
    // 將資料一行一行寫到網頁
    row1 = data[0];
    row2 = data[1];
    // 呼應到網頁的 class = announcemain
    document.getElementById("cardname01").value = row1[0];
    document.getElementById("cardvalue01").value = row2[0];
    document.getElementById("cardname02").value = row1[1];
    document.getElementById("cardvalue02").value = row2[1];
    document.getElementById("cardname03").value = row1[2];
    document.getElementById("cardvalue03").value = row2[2];
    document.getElementById("cardname04").value = row1[3];
    document.getElementById("cardvalue04").value = row2[3];
    document.getElementById("cardname05").value = row1[4];
    document.getElementById("cardvalue05").value = row2[4];
    document.getElementById("cardname06").value = row1[5];
    document.getElementById("cardvalue06").value = row2[5];
    document.getElementById("cardname07").value = row1[6];
    document.getElementById("cardvalue07").value = row2[6];
    document.getElementById("cardname08").value = row1[7];
    document.getElementById("cardvalue08").value = row2[7];
});