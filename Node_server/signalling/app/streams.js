module.exports = function() {
  /**
   * available streams 
   * the id value is considered unique (provided by socket.io)
   */
  var streamList = [];

  /**
   * Stream object
   */
  //아이디와 이름을 전달받음
  var Stream = function(id, name, connect) {
    this.name = name;
    this.id = id;
    this.connect = connect;
  }

  return {
    //스트림 추가할때 //소켓핸들러에서 추가해줌
    addStream : function(id, name, connect) {
      var stream = new Stream(id, name, connect);
     
      //스트림 리스트에 추가
      streamList.push(stream);
    },

    removeStream : function(id) {
      var index = 0;
      while(index < streamList.length && streamList[index].id != id){
        index++;
      }
      streamList.splice(index, 1);
    },

    // update function
    update : function(id, name ,connect) {
      var stream = streamList.find(function(element, i, array) {
        return element.id == id;
      });
      stream.name = name;
      stream.connect = connect;
    },

    getStreams : function() {
      return streamList;
    }
  }
};
