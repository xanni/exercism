# Log line parser exercise
class LogLineParser
  def initialize(line)
    @line = line
  end

  def message = @line.partition(':')[2].strip

  def log_level = @line[1..@line.index(']') - 1].downcase

  def reformat = "#{message} (#{log_level})"
end
