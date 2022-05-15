$(".nextpage").click(function(){
    //Post
    $.ajax({
      url: "/announce_main",
      //成功後的回應
      success: function(rawdata){
        // 取得頁碼轉int
        page = $('.pagenumber').text();
        page = parseInt(page, 10);
        //翻頁
        nextpage = page+1;
        //下頁對應在list的位置
        tail = nextpage * 6;
        head = tail - 6;
        // 取出所有資料
        data = rawdata.data;
        //如果下一頁有資料才會觸發更新
        if (head <= data.length) {
          //清空內容與頁碼
          $('.announcemain').empty();
          $('.pagenumber').empty();
          //更新頁碼
          $('.pagenumber').append(nextpage);
          // 將資料一行一行寫到網頁
          for (let i = head; i < tail; i++) {
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
        }
      }
    });
});