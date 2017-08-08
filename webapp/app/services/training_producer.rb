class TrainingProducer
  def self.publish(message)
    queue.publish(message.to_json)
  end

  def self.queue
    @queue ||= channel.queue("training")
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