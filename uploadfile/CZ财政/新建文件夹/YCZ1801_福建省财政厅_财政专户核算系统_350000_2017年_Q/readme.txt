        var listitem = {};
        var userPic=''
        var username =''
        var nickName=''
        var unreadmsgcount2 = unreadmsgcount(resitem_f.objectId)
        if(resitem_f.executor_pointer){
          userPic = resitem_f.executor_pointer.userPic||''
          username = resitem_f.executor_pointer.username || ''
          nickName = resitem_f.executor_pointer.nickName || ''
        }
        var fl="";
        switch (resitem_f.fl) {
          case "账套导入":
            fl = "账套";
            break;
          case "数据输出":
            fl = "输出";
            break;
          case "数据分析":
            fl = "分析";
            break;
          case "数据采集":
            fl = "采集";
            break;
          case "处内工作":
            fl = "处内";
            break;
          case "其他":
            fl = "其他";
            break;
          default:
            fl = "其他";
        }
        if (resitem_f.complete_pointer){
          var completion = resitem_f.complete_pointer.objectId
        }else{
          var completion = ''
        }
        listitem = { 'objectId': resitem_f.objectId, 'id': resitem_f.index, 'title': resitem_f.title, 'type': resitem_f.type, 'fl': fl, 'completion': completion, 'sqbm': resitem_f.sqbm, 'username': username, 'executor': username, 'nickName': nickName, 'userPic': userPic, 'approval': resitem_f.approval, 'enddate': util.formatTime(resitem_f.enddate), 'createdat': util.formatTime(resitem_f.createdAt), 'unreadmsgcount': unreadmsgcount2||0};
        listall.unshift(listitem);