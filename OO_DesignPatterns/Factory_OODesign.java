package OO_DesignPatterns;

  // -- vehicle interface and implementation Classes --

  interface Vehicle {
    String getType();
  }
  
  class Car implements Vehicle {
    @Override
    public String getType() {
        return "Car";
    }
  }
  
  class Bike implements Vehicle {
    @Override
    public String getType() {
        return "Bike";
    }
  }
  
  class Truck implements Vehicle {
    @Override
    public String getType() {
        return "Truck";
    }
  }

  // -- abstract class VehicleFactory and its subclasses -- 
  
  abstract class VehicleFactory {
    abstract Vehicle createVehicle();
  }
  
  class CarFactory extends VehicleFactory {
    // Write your code here
    @Override
    Vehicle createVehicle(){
        return new Car();
    }
  }
  
  class BikeFactory extends VehicleFactory {
    // Write your code here
    @Override
    Vehicle createVehicle(){
        return new Bike();
    }
  }
  
  class TruckFactory extends VehicleFactory {
    // Write your code here
    @Override
    Vehicle createVehicle(){
        return new Truck();
    }
  }

public class Factory_OODesign {

  public static void main(String[] args) {
    VehicleFactory carFactory = new CarFactory();
    VehicleFactory truckFactory = new TruckFactory();
    VehicleFactory bikeFactory = new BikeFactory();

    Vehicle myCar = carFactory.createVehicle();
    Vehicle myTruck = truckFactory.createVehicle();
    Vehicle myBike = bikeFactory.createVehicle();

    myCar.getType();   // "Car"
    myTruck.getType(); // "Truck"
    myBike.getType();  // "Bike"
  }
  
}
