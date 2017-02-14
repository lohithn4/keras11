# keras12.py

# This script should use Keras and Flask-RESTful to generate stock market predictions.

# Demo:
# export FLASK_DEBUG=1
# ~/anaconda3/bin/python keras12.py

import keras11
import io
import keras
import pdb
import os
import flask         as fl
import flask_restful as fr

application = fl.Flask(__name__)
api         = fr.Api(application)

class Nnmodel(fr.Resource):
  # This method should create a model to predict yr2predict.
  def get(self,local=False, tkr='SPY',yr2predict='2017',yrs2train=10,hlayers=1,neurons=4,features='pctlag1,slope2,moy'):      
    # I should get prices and features for tkr:
    if not local: # I should see fl.request.args
      features = fl.request.args.get('features', 'pctlag1,slope3,dom')
    features_l = features.split(',')
    col_l      = ['cdate','closep','pctlead','updown']+features_l
    pdb.set_trace()
    feat_df    = keras11.genf(tkr)[col_l]    
    return {'nothing':'yet'}

api.add_resource(Nnmodel, '/nnmodel/<tkr>/<yr2predict>/<int:yrs2train>/<int:hlayers>/<int:neurons>')
# curl localhost:5012/nnmodel/IBM/2017/3/2/3?features=pctlag1,slope2,dow,moy

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5012))
    application.run(host='0.0.0.0', port=port)
'bye'

