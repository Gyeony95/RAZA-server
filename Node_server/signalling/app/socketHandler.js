module.exports = function(io, streams) {

  io.on('connection', function(client) {
    console.log('-- ' + client.id + ' joined --');
    client.emit('id', client.id);

    client.on('message', function (details) {
      var otherClient = io.sockets.connected[details.to];

      if (!otherClient) {
        return;
      }
        delete details.to;
        details.from = client.id;
        otherClient.emit('message', details);
    });


    client.on('exchange', function (localid) {
      console.log('테스트 ');
      console.log('상대 아이디 : '+ localid);
      client.emit('exchange',localid);
    });
      
    client.on('readyToStream', function(options) {
      console.log('-- ' + client.id + ' is ready to stream --');
      //고유아이디랑 이름을 스트림을 넘김
      streams.addStream(client.id, options.name, options.connect); 
     
    });
    
    client.on('update', function(options) {
      streams.update(client.id, options.name, true);
      console.log('업뎃 실행'+options.name);
    });

    function leave() {
      console.log('-- ' + client.id + ' left --');
      streams.removeStream(client.id);
    }

    client.on('disconnect', leave);
    client.on('leave', leave);
  });
};