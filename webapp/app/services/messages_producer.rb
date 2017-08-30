class MessagesProducer
  def self.publish(message)
    queue.publish(message)
  end

  def self.queue
    @queue ||= channel.queue("neural_net")
  end

  def self.channel
    @channel ||= connection.create_channel
  end

  def self.connection
    @connection ||= Bunny.new.tap do |connection|
      connection.start
    end
  end
end
