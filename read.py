import model.CustomersModel as cm
import controller.CustomersController as cc

CustomersController = cc.CustomersController(cm)
CustomersController.read()