# Port of Palermo exercise
module Port
  IDENTIFIER = :PALE
  TERMINAL_A = %w[GAS OIL].freeze

  def self.get_identifier(city) = city[0, 4].upcase.to_sym

  def self.get_terminal(ship_identifier) = TERMINAL_A.include?(ship_identifier.to_s[0, 3]) ? :A : :B
end
