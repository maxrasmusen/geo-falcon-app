import falcon

class ThingsResource(object): 
  def on_get(self, req, res): 
    res.status = falcon.HTTP_200
    res.body = ("HELLO")

app = falcon.API()
things = ThingsResource()
app.add_route('/things', things)