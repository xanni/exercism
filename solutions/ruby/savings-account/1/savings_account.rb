# Savings account exercise
module SavingsAccount
  MAX_YEARS = 100

  def self.interest_rate(balance)
    case balance
    when ...0 then 3.213
    when 0...1000 then 0.5
    when 1000...5000 then 1.621
    else 2.475
    end
  end

  def self.annual_balance_update(balance) = balance + (balance * interest_rate(balance) * 0.01)

  def self.years_before_desired_balance(current_balance, desired_balance)
    years = 0
    while current_balance < desired_balance
      current_balance = annual_balance_update(current_balance)
      years += 1
      raise RangeError, "More than #{MAX_YEARS} years" if years > MAX_YEARS
    end

    years
  end
end
