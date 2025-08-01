# Assembly Line exercise
class AssemblyLine
  BASE_RATE = 221

  def initialize(speed)
    success_ratio = case speed
                    when 1..4 then 1
                    when 5..8 then 0.9
                    when 9 then 0.8
                    when 10 then 0.77
                    else raise ArgumentError, 'Speed must be in the range 1..10'
                    end
    @production_rate_per_hour = BASE_RATE * speed * success_ratio
    @working_items_per_minute = @production_rate_per_hour.div 60
  end

  attr_reader :production_rate_per_hour, :working_items_per_minute
end
