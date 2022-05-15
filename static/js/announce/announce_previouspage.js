$(".previouspage").click(function(){
    //使用php Post
    $.ajax({
      url: "/announce_main",
      //成功後的回應
      success: function(rawdata){
        // 取得頁碼轉int
        page = $('.pagenumber').text();
        page = parseInt(page, 10);
        //頁碼大於一才會更新
        if (page>1) {
          //翻頁
          previouspage = page-1;
          //下頁對應在list的位置
          tail = previouspage * 6;
          head = tail - 6;
          // 取出所有資料
          data = rawdata.data;
          //清空內容與頁碼
          $('.announcemain').empty();
          $('.pagenumber').empty();
          //更新頁碼
          $('.pagenumber').append(previouspage);
          
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