# frozen_string_literal: true

module CreatedAt
  class Generator < Jekyll::Generator
    def generate(site)
      items = site.collections['notes'].docs
      items.each do |page|
        if page.data['date']
          # Garante o formato ISO 8601 para fácil ordenação
          timestamp = page.data['date'].is_a?(Time) ? page.data['date'].iso8601 : Time.parse(page.data['date'].to_s).iso8601
          page.data['created_at_timestamp'] = timestamp
        end
      end
    end
  end
end