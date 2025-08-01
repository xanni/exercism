# frozen_string_literal: true

# Simple calculator exercise
class SimpleCalculator
  class UnsupportedOperation < RuntimeError
  end

  ALLOWED_OPERATIONS = %w[+ / *].freeze

  def self.calculate(first_operand, second_operand, operation)
    raise ArgumentError unless [first_operand, second_operand].all? Numeric
    raise UnsupportedOperation unless ALLOWED_OPERATIONS.include? operation

    [first_operand, operation, second_operand, '=',
     first_operand.send(operation, second_operand)].join ' '
  rescue ZeroDivisionError; 'Division by zero is not allowed.'
  end
end
