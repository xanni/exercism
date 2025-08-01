# Assembly Line exercise
class AssemblyLine
  BASE_RATE = 221
  SUCCESS = ([1] * 4) + ([0.9] * 4) + [0.8, 0.77]

  def initialize(speed)
    @speed = speed
  end

  def production_rate_per_hour = BASE_RATE * @speed * SUCCESS[@speed - 1]

  def working_items_per_minute = (production_rate_per_hour / 60).to_i
end
