# Locomotive engineer exercise
class LocomotiveEngineer
  def self.generate_list_of_wagons(*wagons) = wagons

  def self.fix_list_of_wagons(each_wagons_id, missing_wagons)
    [1, *missing_wagons, *each_wagons_id[3..], *each_wagons_id[0, 2]]
  end

  def self.add_missing_stops(route, **stops) = { **route, stops: stops.values }

  def self.extend_route_information(route, more_route_information)
    { **route, **more_route_information }
  end
end
