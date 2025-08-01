# Bird count exercise
class BirdCount
  def self.last_week = [0, 2, 5, 3, 7, 8, 4].freeze

  def initialize(birds_per_day)
    @this_week = birds_per_day
  end

  def yesterday = @this_week[-2]

  def total = @this_week.sum

  def busy_days = @this_week.select { _1 >= 5 }.count

  def day_without_birds? = @this_week.any? 0
end
